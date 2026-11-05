def responseParse(response):
    res = response.choices[0].message.content
    return res