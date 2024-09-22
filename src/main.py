import panel as pn

pn.extension()



template = pn.template.MaterialTemplate(
    title='ML Interview Quiz',
    # sidebar=[
    #     pn.panel("teste")
    # ],
)
# Append a layout to the main area, to demonstrate the list-like API
template.main.append(
    pn.Row(
        pn.Card( pn.panel("Question 1" ), title="Question" )
    )
)

template.servable();