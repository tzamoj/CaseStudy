import pandas


def as_seconds(dt_arr):
    return (dt_arr - pandas.to_datetime(dt_arr.dt.date)).dt.total_seconds()


def prepare_data(data):
    grps = data.groupby([data["datetime"].dt.date, data["run"]])
    duration = grps["datetime"].max() - grps["datetime"].min()
    duration = duration.dt.total_seconds()
    duration.name = "duration"
    dow = grps["datetime"].apply(lambda s: s.iloc[0].dayofweek)
    dow.name = "dow"
    time = as_seconds(grps["datetime"].min())
    time.name = "time"
    return pandas.concat([dow, time, duration], axis=1)
