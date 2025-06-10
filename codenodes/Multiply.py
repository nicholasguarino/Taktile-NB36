def multiply(data):
    """Function that summarized cols a and b"""

    data["sum"] = data["a"] * data["b"]

    return data


if __env:  # indicates we are running on Taktile
    data = add(data)


#Adding an additional note to test the workflow. Testing again.