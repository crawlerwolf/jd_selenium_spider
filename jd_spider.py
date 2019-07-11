# -*- coding: utf-8 -*-
# author = minjie
import json

import requests
from scrapy import Selector


def parse_good(good_id):
    good_url = 'https://item.jd.com/{}.html'.format(good_id)
    html = requests.get(good_url).text
    sel = Selector(text=html)
    name = ''.join(sel.xpath('//div[@class="sku-name"]/text()').extract()).strip()

    # 获取商品的价格
    price_url = 'https://p.3.cn/prices/mgets?type=1&pdtk=&skuIds=J_{}&source=item-pc'.format(good_id)
    price_text = requests.get(price_url).text
    price_list = json.loads(price_text)
    if price_list:
        price = float(price_list[0]["p"])

    # 获取商品的评价信息
    evaluate_url = 'https://sclub.jd.com/comment/productPageComments.action?productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'.format(good_id, 0)
    evaluate_text = requests.get(evaluate_url).text
    evaluate_json = json.loads(evaluate_text)
    max_page = 0
    if evaluate_json:
        max_page = evaluate_json["max_page"]
        statistics = evaluate_json["hotCommentTagStatistics"]
        summary = evaluate_json["productCommentSummary"]
        evaluate = evaluate_json["comments"]


if __name__ == "__main__":
    parse_good(4356700)
