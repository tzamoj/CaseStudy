import pandas


def read_data(conn, sep=','):
    data = pandas.read_csv(conn, sep=sep)
    data["datetime"] = pandas.to_datetime(data["datetime"])
    return data
