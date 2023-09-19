# Importing library
import qrcode


def generate_qrcode(data, name: str, link: str):
    room_id = link.split('/')[-1]
    name = f"{name}-{room_id}-qrcode"

    # Checking if qr code exists
    # try:
    print(name)
    img = qrcode.make(data)
    img.save(f'app/static/qr/f{name}.png')
    return {'status': 'success'}
    # except:
    #     with open(f'static/f{name}.png', 'rb') as f:
    #         print('exists')
    #         return {'status': 'success'}


def url_shortener(url_shorter, name: str):
    import requests

    url = "https://url-shortener-service.p.rapidapi.com/shorten"

    payload = {"url": url_shorter}
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "69bc405e5bmsh2f4565ba236cd4bp1ea962jsne4eb459bbc5c",
        "X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    try:
        link = response.json()['result_url']
    except:
        link = url_shorter

    return link


def create_qrcode(url, name):
    print('url', url)
    print('name', name)
    link = url_shortener(url, name)
    generate_qrcode(link, name, url)
    return {'status': 'success'}


if __name__ == '__main__':
    print(create_qrcode('http://213.230.69.57:8888/invernment/room/2', 'test'))
