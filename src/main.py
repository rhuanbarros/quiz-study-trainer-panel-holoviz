import panel as pn
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

from supabase import create_client, Client

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]

supabase: Client = create_client(url, key)

data, count = supabase.table('get_question').select("*").execute()
# print(data)
question = data[1][0]

# pn.extension()
pn.extension('mathjax')



template = pn.template.MaterialTemplate(
    title='ML Interview Quiz',
    # sidebar=[
    #     pn.panel("teste")
    # ],
)
# Append a layout to the main area, to demonstrate the list-like API
template.main.append(
    pn.Column(
        pn.Card( pn.pane.Markdown( question["question"] ), 
                title="Question",
                # hide_header=True,
                collapsible=False,
        ),
        pn.Card( 
            # pn.widgets.Button(name='A', button_type='default'),
                pn.pane.Markdown( question["answer_a"] ), 
                title="Option A",
                # hide_header=True,
                collapsible=False,
        ),
        pn.Card( pn.pane.Markdown( question["answer_b"] ), 
                title="Option B",
                # hide_header=True,
                collapsible=False,
        ),
        pn.Card( pn.pane.Markdown( question["answer_c"] ), 
                title="Option C",
                # hide_header=True,
                collapsible=False,
        ),
        pn.Card( pn.pane.Markdown( question["answer_d"] ), 
                title="Option D",
                # hide_header=True,
                collapsible=False,
        ),
        pn.widgets.Button(name='I dont know', button_type='primary')
    )
)

template.servable();