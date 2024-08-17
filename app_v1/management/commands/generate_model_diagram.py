import os
import django
import pydot
from django.apps import apps
from pydot import Node, Edge, Dot
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import models
import sys

'''
Usage:
    python manage.py generate_model_diagram --format=png --output=./models.png --style=variant2 --include-abstract
'''

# Set the default encoding for stdout
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

# Initialize Django settings and environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_core.settings")
django.setup()

class Command(BaseCommand):
    help = 'Generates a diagram of all models and their relationships with multiple UI variants.'

    def add_arguments(self, parser):
        parser.add_argument('--format', type=str, default='png', help='Output format (png, svg, etc.)')
        parser.add_argument('--output', type=str, help='Path to save the output file')
        parser.add_argument('--style', type=str, choices=['variant1', 'variant2', 'variant3', 'variant4', 'variant5', 'variant6'], default='variant1', help='Choose a visual style variant')
        parser.add_argument('--title', type=str, help='Title of the diagram')
        parser.add_argument('--include-abstract', action='store_true', help='Include abstract models in the diagram')

    def handle(self, *args, **options):
        output_format = options['format']
        output_path = options['output'] or os.path.join(settings.BASE_DIR, f"model_diagram.{output_format}")
        style_variant = options['style']
        include_abstract = options['include_abstract']

        # Generate the model graph
        self.generate_model_graph(output_path, output_format, style_variant, include_abstract)
        self.stdout.write(self.style.SUCCESS(f"Model diagram generated successfully at {output_path}."))

    def generate_model_graph(self, output_path, output_format, style_variant, include_abstract):
        # Create a new graph
        graph = Dot(graph_type='digraph', bgcolor="#F5F5F5", fontname="Arial", fontsize="12", rankdir="LR")
        graph.set_graph_defaults(fontsize="12", fontname="Arial")

        # Add title node
        self.add_title_node(graph, title="Django Models Diagram")

        # Add model nodes and edges
        for model in apps.get_models():
            if not include_abstract and model._meta.abstract:
                continue

            self.add_model_node(graph, model, style_variant)
            self.add_model_edges(graph, model, style_variant)

        # Add legend to the diagram
        self.add_legend(graph)

        # Set the size for PNG output with high resolution
        if output_format == 'png':
            graph.set_graph_defaults(size="30,20")  # Sets the graph size in inches for high resolution

        # Write the graph to a file
        graph.write(output_path, format=output_format, encoding='utf-8')

    def add_title_node(self, graph, title=None):
        title_node = Node("title", label=f"{title}", shape="plaintext", fontname="Arial", fontsize="18", fontcolor="#000000", style="bold", bgcolor="#003366")
        graph.add_node(title_node)

    def add_model_node(self, graph, model, style_variant):
        fields = [self.format_field(field) for field in model._meta.fields if field.name != 'id']
        label = self.get_table_label(model._meta.object_name, fields, style_variant)

        node = Node(model._meta.object_name, shape="box", style="filled", fillcolor="#F0F0F0",
                    fontname="Arial", fontsize="10", width="2.0", height="1.0", color="#DCDCDC", label=label)
        graph.add_node(node)

    def add_model_edges(self, graph, model, style_variant):
        for field in model._meta.fields:
            if isinstance(field, models.ForeignKey):
                self.add_edge(graph, model._meta.object_name, field.related_model._meta.object_name, "1-n", "#9CFF9C", "#388E3C", style_variant)
            elif isinstance(field, models.OneToOneField):
                self.add_edge(graph, model._meta.object_name, field.related_model._meta.object_name, "1-1", "#F08080", "#C62828", style_variant)

        for field in model._meta.many_to_many:
            self.add_edge(graph, model._meta.object_name, field.related_model._meta.object_name, "n-n", "#87CEFA", "#1976D2", style_variant)

    def add_edge(self, graph, source, target, label, color, fontcolor, style_variant):
        edge = Edge(source, target, color=color, label=label, fontcolor=fontcolor, fontsize="10", style="bold", dir="forward")
        graph.add_edge(edge)

    def format_field(self, field):
        if isinstance(field, models.ForeignKey):
            datatype = field.related_model._meta.object_name
        else:
            datatype = field.get_internal_type()
        return f"<tr><td align='left'>{field.name}</td><td align='left'>{datatype}</td></tr>"

    def get_table_label(self, model_name, fields, style_variant):
        if style_variant == 'variant1':
            return f"<<table border='0' cellborder='1' cellspacing='0' bgcolor='#FFFFFF'>" \
                   f"<tr><td colspan='2' bgcolor='#4682B4' fontcolor='white' fontname='Arial' fontsize='14' align='center'><b>{model_name}</b></td></tr>" \
                   f"<tr><td bgcolor='#E0E0E0' fontcolor='#000000' fontname='Arial' fontsize='12'><b>Field</b></td>" \
                   f"<td bgcolor='#E0E0E0' fontcolor='#000000' fontname='Arial' fontsize='12'><b>Datatype</b></td></tr>" \
                   f"{''.join(fields)}</table>>"
        elif style_variant == 'variant2':
            return f"<<table border='0' cellborder='1' cellspacing='0' bgcolor='#F8F9FA'>" \
                   f"<tr><td colspan='2' bgcolor='#007BFF' fontcolor='white' fontname='Arial' fontsize='14' align='center'><b>{model_name}</b></td></tr>" \
                   f"<tr><td bgcolor='#E9ECEF' fontcolor='#000000' fontname='Arial' fontsize='12'><b>Field</b></td>" \
                   f"<td bgcolor='#E9ECEF' fontcolor='#000000' fontname='Arial' fontsize='12'><b>Datatype</b></td></tr>" \
                   f"{''.join(fields)}</table>>"
        elif style_variant == 'variant3':
            return f"<<table border='0' cellborder='1' cellspacing='0' bgcolor='#FFFFFF'>" \
                   f"<tr><td colspan='2' bgcolor='#E0EEED' fontcolor='white' fontname='Arial' fontsize='14' align='center'><b>{model_name}</b></td></tr>" \
                   f"<tr><td bgcolor='#E0E0E0' fontcolor='#000000' fontname='Arial' fontsize='12'><b>Field</b></td>" \
                   f"<td bgcolor='#E0E0E0' fontcolor='#000000' fontname='Arial' fontsize='12'><b>Datatype</b></td></tr>" \
                   f"{''.join(fields)}</table>>"

    def add_legend(self, graph):
        legend = Node("legend", label="Legend:\n1-n: ForeignKey\n1-1: OneToOneField\nn-n: ManyToManyField",
                      shape="rect", style="filled", fillcolor="#FFFFFF", fontname="Arial", fontsize="12", width="3", height="2", color="#DCDCDC")
        graph.add_node(legend)
        # Position the legend node
        legend.set_pos("0,0!")
