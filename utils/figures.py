import plotly.express as px

def plot_family_size(data):
    fig = px.histogram(data, x = 'family_size' )
    #fig.update_layout(bargap = 1, yaxis_title = "passengers")
    return fig

def plot_outcome(data):
    outcome = data['survived'].value_counts()
    fig = px.pie(names =['died', 'survived'], values = outcome.values,  hole=0.4)
    return fig