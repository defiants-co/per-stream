# from perpstream.gmx.client import GmxArbitrumClient
# client = GmxArbitrumClient()


# my_positions = []

# def print_positons(old_positions, new_positions):
#     print(old_positions, new_positions)

# client.poll_positions(
#     user_id="0xeF5b5616FBa4e4d30a6B74De2B912025F8e627E4",
#     time_wait_seconds=0,
#     debug=True,
#     callback=print_positons
# )


dydx_addresses = [
    "dydx1ynqp0k273fjg7kjs6d5zm34sllv9z384ycztux",
    "dydx1fx9qt7rw3d2l2u0ut72fh204s60mr29wukksrr",
    "dydx1f3dnxu7l809knnzac4h9qnfmxqp4pm589sg9eq",
    "dydx1fv0ewuq7e7c3h6fwtsrl6fsx3rqgyfc640grf8",
    "dydx164yt5a74vhpm5llyyz0mcwlfu8g7ufevgazl2v",
    "dydx1axw38e0a46app77tphswrhmrxh500tvhchu38d",
    "dydx1ryhl4xy25hgmyea4gys3jjfxyllglwm6kxlf4p",
    "dydx14d5mwxu3f7j5pm0wa842yx06sem8ynw6j7d8cj",
    "dydx1xdxhh6pg75rxjzrgf5m38s5m2rpec6am0uj87q",
    "dydx1vf9kmsgqyuuznq9uysmc6f3r6kf7dj8dns5x7u",
    "dydx1m0d032jdac8y0xt2375m3ywkjczfftk2zy09en",
    "dydx1y7378t0lppdqq5lgu2qgjuymk7zamn08v3cjeu",
    "dydx1jerkajy78g5wqgu0psglw98edzmf9um47dmgq9",
    "dydx155586dv220psvtaycw3us8am2twn9uj8tg353r",
    "dydx144rcvrufrlqnfa7jzxhur7hjudpy7hnvyw6ghx",
    "dydx1fmycul4c3w8lwp463nxgj4kwcwmll0epusma7v",
    "dydx1qe457x9d5rny8twcgkwmcpcgs2m65d6t6n4xem",
    "dydx1ru82r52s7tcgxqz92e5qh7az2qss8m2l9a9um4",
    "dydx1x0cjspuhye38343ewwed5cjdhhzejfgtusl3yn",
    "dydx13hrf4zuka03ew2064gmmsa9qvxcgm2nsg74zkj",
    "dydx1rt2pjyr830plssddl9e3h765k5fc8d4xw46ry7",
    "dydx1j7t5jnvf8dl3wjgu5jh4vrkpvfx750r4w4n0up",
    "dydx18z8x73ecgpzv33pcqk7szjt6uuu2lppyqsmfqd",
    "dydx17qzyy38tqyrzvryvusn2vk8phyldc6y3tqtwnc",
    "dydx12u2xq9vgy087zngm60luvs7kkl9cquldt6u2n0",
    "dydx122tkkqkc8ue374mhpf6qv2g7w9zzdqs7t6kgrf",
    "dydx1pu079gzs7l8a763k69cxtjha6aezs9u498mapx",
    "dydx184f5wh3t6fhvrqvqztupug08m6wfvw5sd0suxe",
    "dydx1unga99ldhcafpf563hu547ahmwv7flnxmr0979",
    "dydx146m656dghalgr30stn9zwp5rrs2lh0puzf2zes",
    "dydx1tapx759aplrelza2kyvc5xcg6j6yrv7nz6ccqz",
    "dydx17e30pydxf2wdwwr8e24jwke6qmdwv8906easkj",
    "dydx1m8c2hxtl4sx7sgyf0np3mtl4scnqz5jtl4zzkd",
    "dydx19uadmfmc8r0wrjz264hghl7yyhsuh8xwxyzylx",
    "dydx1tqddjth9rzxya3kkd26ttte04nm989tjq5vd8z",
    "dydx15f3cqd9qfhl7cey3sqwkp6e5pxrmg7frq9gcl4",
    "dydx1txwq0f5pnkmmnuclg09s47calzaf8gst6l3ruy",
    "dydx1jycfuenykjjvykv2n8erf7aluureg3kql4evp4",
    "dydx1zg3hlxpyq4mrd9xggqcrnjpr6q8lcyzn3629nk",
    "dydx1756k9kf0dcjx3j6p8jycvuqnuyun6vtyd96jpl",
    "dydx1jf0y400uf9ux0xswfwv3ekdptmmvakzvwj7zmc",
    "dydx1hw3zk7mcr5fvzax05x82n75hrktpp49pkluzhr",
    "dydx1xxl6c5nshfeklraz3f92dpyakg09mmn9vp5dym",
    "dydx14g4rna3u7judm6hnm8rg4e355mwu0e8kres4te",
    "dydx1s7e9jq0rmwjxx7f9nnru8cxdx3rfjftwwuwsk9",
    "dydx1scvlue4z3p45cuf9l27d0yehw53lx4944tm5c8",
    "dydx1snz07uvh6epg9fc2skdud7g8jyuvtqh0t8mxdy",
    "dydx146aerc425pzl5c2j6esfvkc44ypv4e2lr4kck7",
    "dydx10wzu64wmwrnuvka6vk3rspgdl8vg9lz3mfgr83",
    "dydx1n3gas4dz9vmex9cg7gl2spa24dhkr65fmq2vp2",
    "dydx1h94vyztjrp4t6m6vymnfaq9zt9ww5snfqqxhzn",
    "dydx12vv9265mudcxrn6fdy4h253lhz7xwtyy0zk7wc",
    "dydx1dxn9d3684l44gl83gsgudfdrh34sz5glp5npxy",
    "dydx1a4c47rmcnf9ah58045tpsv5gnlvxxw0xcrlysa",
    "dydx1yj7nhdpvxlf5y4yh0z69ccjmv54t7zymkpht0x",
    "dydx1kvhkq0u7m5zmyepjvv9xsll3ve26xkxkks5xhe",
    "dydx1rqvpzwjulzm3gz6c9gf63m00gdskk8x94a8mwl",
    "dydx18mu3sj0qtmjvulmgrjcxu52ctrwlf4nceu4f62",
    "dydx17up03uwtd74whyffnkfn24mjuyl2y4hury9hus",
    "dydx1tdwk8y0sfvn3yhfv4etwpyjyyn3526f72d57t9",
    "dydx1f5lswk8ettlyjuxdu9ap6xuaxzqptpcea3kex6",
    "dydx1v7qgpqj6uq9s55p9wsz5csr95qas97naxc3a99",
    "dydx1q8cednyr7sdy5s0u4jgvyh3de4nzt8078de3nu",
    "dydx1wv798lsp2z8xa5syzahx9s0fkz4u4we9kuemqf",
    "dydx1mg8vknwn08y783fz6ld074prmwqcwvqtv3lvnu",
    "dydx1s9q4vcyel46z2c3lx7tsk8dh6ma06zqwwt2yh9",
]
from perpstream.dydx.client import DydxClient
from time import sleep
# dydx1d06lgyy03spureacp933g3qc3wwuszaxjurk5w
client = DydxClient()
all_positions = []
for address in dydx_addresses:
    try:
        all_positions += client.fetch_positions(address)
    except KeyboardInterrupt:
        break

    except:
        pass

import json

with open('positions.json', 'w') as file:
    json.dump([position.json() for position in all_positions], file, indent=4)
