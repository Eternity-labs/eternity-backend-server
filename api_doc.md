http://ip:port/token/substrate/erc20distribute

返回erc20链上代币的分布情况

**Methods: GET**

**Return Body**

```json
[
    {
        "address":"0xx12341",
        "Num":"2313",
    },
    {
        "address":"0x124591",
        "Num":"2313",
    },
    {
        "address":"0x859901",
        "Num":"2313",
    },
    {
        "address":"0x0884904",
        "Num":"2313",
    }
]
```





http://ip:port/token/substrate/kmanserc20

返回erc20链上代币持币聚类信息

**Methods : GET**

**Return Body**

```json
[
        {
            "Erc20Class": "A",
            "Totalnum": 2000
        },
        {
            "Erc20Class": "B",
            "Totalnum": 2001231
        },
        {
            "Erc20Class": "C",
            "Totalnum": 2015
        },
        {
            "Erc20Class": "D",
            "Totalnum": 12000
        },
        {
            "Erc20Class": "E",
            "Totalnum": 978000
        }
    ]
```







http://ip:port/verify/substrate/listnodeinfo

http://ip:port/analiysis/substrate/listnodeinfo

http://ip:port/dispatch/substrate/listnodeinfo

http://ip:port/quantize/substrate/listnodeinfo

返回节点的信息

**Methods: GET**

**Return Body**

```json
[
    {
        "name":"Axxx",
        "IP": "127.0.0.1:9000",
        "Status": "online",
        "AccountId": "0x123156184",
    },
    {
        "name":"Bxxx",
        "IP": "127.0.0.1:9000",
        "Status": "offline",
        "AccountId": "0x123156184",
    },
    {
        "name":"Cxxx",
        "IP":"127.0.0.1:9000",
        "Status": "online",
        "AccountId":"0x123156184",

    },
    {
        "name":"Axxx",
        "IP": "127.0.0.1:9000",
        "Status": "online",
        "AccountId": "0x123156184",
    },
    {
        "name":"Axxx",
        "IP": "127.0.0.1:9000",
        "Status": "online",
        "AccountId": "0x123156184",
    },
]
```





http://ip:port/quantize/modellist

返回链上模型

**methods: GET**

**Return Body**

```json
[
    {
        "Name": "A",
        "Ipfshash": "0x1234131",
        "AccountId": "gegwegwetg23234"
    },
    {
        "Name": "B",
        "Ipfshash": "0x1234131",
        "AccountId": "qwgqgwqgwert34t23"
    },
    {
        "Name": "C",
        "Ipfshash": "0x1234131",
        "AccountId": "ereryert3414121"
    },
    {
        "Name": "D",
        "Ipfshash": "0x1234131",
        "AccountId": "qwgqwgqwe12312qgddbh"
    },
    {
        "Name": "E",
        "Ipfshash": "0x1234131",
        "AccountId": "1231qwfqwgqg14"
    },
    {
        "Name": "F",
        "Ipfshash": "0x1234131",
        "AccountId": "wegqwgqwgwweqwe"
    },
]
```







http://ip:port/user/accountinfo/<address>

返回链上用户的信息.以及正在量化的节点信息

**Methods GET**

**Return Body**

```json
{
        "AccountId": "0x11233121",
        "Token": "108591",
        "Income": "9999",
        "Quan": [
            {
                "model": "A",
                "Value": "100",
                "quanNode": "0x123411"
            },
            {
                "model": "A",
                "Value": "100",
                "quanNode": "0x123411"
            },
            {
                "model": "A",
                "Value": "100",
                "quanNode": "0x123411"
            },
            {
                "model": "A",
                "Value": "100",
                "quanNode": "0x123411"
            },
            {
                "model": "A",
                "Value": "100",
                "quanNode": "0x123411"
            },
            {
                "model": "A",
                "Value": "100",
                "quanNode": "0x123411"
            },

]
}
```