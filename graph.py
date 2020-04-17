import plotly.express as px
import pandas

from data import fetch_data

if __name__ == "__main__":
    cases_list = fetch_data()
    for i, data in enumerate(cases_list):
        data["day"] = i + 1
        data["active"] = data["confirmed"] - data["recovered"] - data["deaths"]

    # df = px.data.gapminder().query("continent=='Oceania'")
    # print(df)

    wide_df = pandas.DataFrame(cases_list)
    tidy_df = wide_df.melt(
        id_vars="day",
        value_vars=("confirmed", "deaths", "recovered", "active"),
        var_name="type",
        value_name="cases"
    )

    fig = px.line(tidy_df, x="day", y="cases", color="type")

    fig.update_layout(
        title="Covid-19 cases in Poland",
        xaxis_title="Days since first case",
        yaxis_title="Number of cases",
        font=dict(
            family="Arial, monospace",
            size=18,
            color="#7f7f7f"
        )
    )

    fig.show()
