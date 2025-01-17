# from tweet_manager import TweetManager
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html

def filter(search_query):
    # ranked_tweets = TweetManager.extract_tweets(search_query)
    ranked_tweets = ["dONALD DUCK"]
    return ranked_tweets


def geospatial_graph():
    df = px.data.gapminder().query("year==2007")
    fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
    # fig.show()
    # fig.write_html("1.html")
    return html.Div([dcc.Graph(figure=fig)])


if __name__ == "__main__":
    print(filter("trump"))