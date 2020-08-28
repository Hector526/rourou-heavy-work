# -*- coding: UTF-8 -*
import os
import pandas as pd
import utils

source_url = "." + os.sep + "source"
target_url = "." + os.sep + "target"


def country_thisMonth(df):
    print("****************************************************")
    print("当月：")
    # 统计当月优Ⅲ停运站点
    good_water_decommissioned_sites = df[df["前五项水质类别"] == "停运"]
    nameStr = ""
    for index, row in good_water_decommissioned_sites.iterrows():
        nameStr += row["省平台名称"] + row["断面名称"] + "、"
    print("优Ⅲ停运：")
    decommissioned_num = str(len(good_water_decommissioned_sites))
    print("优Ⅲ停运站点数：" + decommissioned_num)
    decommissioned_name = nameStr[:-1]
    print("优Ⅲ停运站点名称：" + decommissioned_name)
    # print("优Ⅲ停运站点详情：")
    # print(good_water_decommissioned_sites)
    print("---------------------------------------------------")

    # 预处理
    good_water_df = df[df["前五项水质类别"] != "停运"]
    good_water_df.insert(loc=0, column='优Ⅲ', value=good_water_df.apply(
        utils.country_goodWater, axis='columns'))
    good_water_df.insert(loc=0, column='合格', value=good_water_df.apply(
        utils.country_expectedWater, axis='columns'))
    good_water_sum = len(good_water_df)

    # 统计优Ⅲ
    good_water_count = dict(good_water_df["优Ⅲ"].value_counts())
    print("优Ⅲ统计：")
    print("总数：" + str(good_water_sum) + " 优Ⅲ：" +
          str(good_water_count[1]) + " 否：" + str(good_water_count[0]))
    good_water_scale = round((good_water_count[1] / good_water_sum), 3)
    print("优Ⅲ比例：" + str(good_water_scale))
    print("---------------------------------------------------")

    # 统计合格
    expected_water_count = dict(good_water_df["合格"].value_counts())
    print("合格统计：")
    print("总数：" + str(good_water_sum) + " 合格：" +
          str(expected_water_count[1]) + " 否：" + str(expected_water_count[0]))
    expected_water_scale = round(
        (expected_water_count[1] / good_water_sum), 3)
    print("合格比例：" + str(expected_water_scale))

    # 未达标统计below quality
    below_quality_sites = good_water_df[good_water_df["合格"] == 0]
    below_quality_name = ""
    for index, row in below_quality_sites.iterrows():
        below_quality_name += row["省平台名称"] + row["断面名称"] + "、"
    below_quality_num = str(expected_water_count[0])
    print("未达标断面数：" + below_quality_num)
    below_quality_name_str = below_quality_name[:-1]
    print("未达标断面名称：" + below_quality_name_str)
    print("---------------------------------------------------")
    seq = "\n"
    result = "****************************************************" + seq
    result += "当月：" + seq
    result += "优Ⅲ停运：" + seq 
    result += "优Ⅲ停运站点数：" + decommissioned_num + seq 
    result += "优Ⅲ停运站点名称：" + decommissioned_name + seq
    result += "---------------------------------------------------" + seq
    result += "优Ⅲ统计：" + seq 
    result += "总数：" + str(good_water_sum) + " 优Ⅲ：" + str(good_water_count[1]) + " 否：" + str(good_water_count[0]) + seq
    result += "优Ⅲ比例：" + str(good_water_scale) + seq
    result += "---------------------------------------------------" + seq
    result += "合格统计：" + seq
    result += "总数：" + str(good_water_sum) + " 合格：" + str(expected_water_count[1]) + " 否：" + str(expected_water_count[0]) + seq
    result += "合格比例：" + str(expected_water_scale) + seq
    result += "未达标断面数：" + below_quality_num + seq
    result += "未达标断面名称：" + below_quality_name_str + seq
    result += "---------------------------------------------------" + seq

    return result

def country_yearOnyear(df):
    print("****************************************************")
    print("同比：")
    # 统计当月优Ⅲ停运站点
    good_water_decommissioned_sites = df[df["同比（自动）"] == "停运"]
    nameStr = ""
    for index, row in good_water_decommissioned_sites.iterrows():
        nameStr += row["省平台名称"] + row["断面名称"] + "、"
    print("优Ⅲ停运：")
    decommissioned_num = str(len(good_water_decommissioned_sites))
    print("优Ⅲ停运站点数：" + decommissioned_num)
    decommissioned_name = nameStr[:-1]
    print("优Ⅲ停运站点名称：" + decommissioned_name)
    # print("优Ⅲ停运站点详情：")
    # print(good_water_decommissioned_sites)
    print("---------------------------------------------------")

    # 预处理
    good_water_df = df[df["同比（自动）"] != "停运"]
    good_water_df.insert(loc=0, column='优Ⅲ', value=good_water_df.apply(
        utils.country_goodWater_yearOnyear, axis='columns'))
    good_water_df.insert(loc=0, column='合格', value=good_water_df.apply(
        utils.country_expectedWater_yearOnyear, axis='columns'))
    good_water_sum = len(good_water_df)

    # 统计优Ⅲ
    good_water_count = dict(good_water_df["优Ⅲ"].value_counts())
    print("优Ⅲ统计：")
    print("总数：" + str(good_water_sum) + " 优Ⅲ：" +
          str(good_water_count[1]) + " 否：" + str(good_water_count[0]))
    good_water_scale = round((good_water_count[1] / good_water_sum), 3)
    print("优Ⅲ比例：" + str(good_water_scale))
    print("---------------------------------------------------")

    # 统计合格
    expected_water_count = dict(good_water_df["合格"].value_counts())
    print("合格统计：")
    print("总数：" + str(good_water_sum) + " 合格：" +
          str(expected_water_count[1]) + " 否：" + str(expected_water_count[0]))
    expected_water_scale = round(
        (expected_water_count[1] / good_water_sum), 3)
    print("合格比例：" + str(expected_water_scale))

    # 未达标统计below quality
    below_quality_sites = good_water_df[good_water_df["合格"] == 0]
    below_quality_name = ""
    for index, row in below_quality_sites.iterrows():
        below_quality_name += row["省平台名称"] + row["断面名称"] + "、"
    below_quality_num = str(expected_water_count[0])
    print("未达标断面数：" + below_quality_num)
    below_quality_name_str = below_quality_name[:-1]
    print("未达标断面名称：" + below_quality_name_str)
    print("---------------------------------------------------")

    seq = "\n"
    result = "****************************************************" + seq
    result += "同比：" + seq
    result += "优Ⅲ停运：" + seq 
    result += "优Ⅲ停运站点数：" + decommissioned_num + seq 
    result += "优Ⅲ停运站点名称：" + decommissioned_name + seq
    result += "---------------------------------------------------" + seq
    result += "优Ⅲ统计：" + seq 
    result += "总数：" + str(good_water_sum) + " 优Ⅲ：" + str(good_water_count[1]) + " 否：" + str(good_water_count[0]) + seq
    result += "优Ⅲ比例：" + str(good_water_scale) + seq
    result += "---------------------------------------------------" + seq
    result += "合格统计：" + seq
    result += "总数：" + str(good_water_sum) + " 合格：" + str(expected_water_count[1]) + " 否：" + str(expected_water_count[0]) + seq
    result += "合格比例：" + str(expected_water_scale) + seq
    result += "未达标断面数：" + below_quality_num + seq
    result += "未达标断面名称：" + below_quality_name_str + seq
    result += "---------------------------------------------------" + seq

    return result

def country_monthOnmonth(df):
    print("****************************************************")
    print("环比：")
    # 统计当月优Ⅲ停运站点
    good_water_decommissioned_sites = df[df["环比（自动）"] == "停运"]
    nameStr = ""
    for index, row in good_water_decommissioned_sites.iterrows():
        nameStr += row["省平台名称"] + row["断面名称"] + "、"
    print("优Ⅲ停运：")
    decommissioned_num = str(len(good_water_decommissioned_sites))
    print("优Ⅲ停运站点数：" + decommissioned_num)
    decommissioned_name = nameStr[:-1]
    print("优Ⅲ停运站点名称：" + decommissioned_name)
    # print("优Ⅲ停运站点详情：")
    # print(good_water_decommissioned_sites)
    print("---------------------------------------------------")

    # 预处理
    good_water_df = df[df["环比（自动）"] != "停运"]
    good_water_df.insert(loc=0, column='优Ⅲ', value=good_water_df.apply(
        utils.country_goodWater_monthOnmonth, axis='columns'))
    good_water_df.insert(loc=0, column='合格', value=good_water_df.apply(
        utils.country_expectedWater_monthOnmonth, axis='columns'))
    good_water_sum = len(good_water_df)

    # 统计优Ⅲ
    good_water_count = dict(good_water_df["优Ⅲ"].value_counts())
    print("优Ⅲ统计：")
    print("总数：" + str(good_water_sum) + " 优Ⅲ：" +
          str(good_water_count[1]) + " 否：" + str(good_water_count[0]))
    good_water_scale = round((good_water_count[1] / good_water_sum), 3)
    print("优Ⅲ比例：" + str(good_water_scale))
    print("---------------------------------------------------")

    # 统计合格
    expected_water_count = dict(good_water_df["合格"].value_counts())
    print("合格统计：")
    print("总数：" + str(good_water_sum) + " 合格：" +
          str(expected_water_count[1]) + " 否：" + str(expected_water_count[0]))
    expected_water_scale = round(
        (expected_water_count[1] / good_water_sum), 3)
    print("合格比例：" + str(expected_water_scale))

    # 未达标统计below quality
    below_quality_sites = good_water_df[good_water_df["合格"] == 0]
    below_quality_name = ""
    for index, row in below_quality_sites.iterrows():
        below_quality_name += row["省平台名称"] + row["断面名称"] + "、"
    below_quality_num = str(expected_water_count[0])
    print("未达标断面数：" + below_quality_num)
    below_quality_name_str = below_quality_name[:-1]
    print("未达标断面名称：" + below_quality_name_str)
    print("---------------------------------------------------")

    seq = "\n"
    result = "****************************************************" + seq
    result += "环比：" + seq
    result += "优Ⅲ停运：" + seq 
    result += "优Ⅲ停运站点数：" + decommissioned_num + seq 
    result += "优Ⅲ停运站点名称：" + decommissioned_name + seq
    result += "---------------------------------------------------" + seq
    result += "优Ⅲ统计：" + seq 
    result += "总数：" + str(good_water_sum) + " 优Ⅲ：" + str(good_water_count[1]) + " 否：" + str(good_water_count[0]) + seq
    result += "优Ⅲ比例：" + str(good_water_scale) + seq
    result += "---------------------------------------------------" + seq
    result += "合格统计：" + seq
    result += "总数：" + str(good_water_sum) + " 合格：" + str(expected_water_count[1]) + " 否：" + str(expected_water_count[0]) + seq
    result += "合格比例：" + str(expected_water_scale) + seq
    result += "未达标断面数：" + below_quality_num + seq
    result += "未达标断面名称：" + below_quality_name_str + seq
    result += "---------------------------------------------------" + seq

    return result

def main_countryFile(df, sheet_name):
    file_name = target_url + os.sep + "国考-" + sheet_name + ".txt"
    print(file_name)

    text_thisMonth = country_thisMonth(df)
    text_yearOnyear = country_yearOnyear(df)
    text_monthOnmonth = country_monthOnmonth(df)

    with open(file_name, "a") as file:
        file.write(text_thisMonth)
        file.write(text_yearOnyear)
        file.write(text_monthOnmonth)
        file.close()


def main_provinceFile(df, sheet_name):
    file_name = target_url + os.sep + "省考-" + sheet_name + ".txt"
    print(file_name)

    # 预处理
    good_water_df = df
    good_water_df.insert(loc=0, column='优Ⅲ', value=good_water_df.apply(
        utils.province_goodWater, axis='columns'))
    good_water_df.insert(loc=0, column='合格', value=good_water_df.apply(
        utils.province_expectedWater, axis='columns'))
    good_water_sum = len(good_water_df)

    # 统计优Ⅲ
    good_water_count = dict(good_water_df["优Ⅲ"].value_counts())
    print("优Ⅲ统计：")
    print("总数：" + str(good_water_sum) + " 优Ⅲ：" +
          str(good_water_count[1]) + " 否：" + str(good_water_count[0]))
    good_water_scale = round((good_water_count[1] / good_water_sum), 3)
    print("优Ⅲ比例：" + str(good_water_scale))
    print("---------------------------------------------------")

    # 统计合格
    expected_water_count = dict(good_water_df["合格"].value_counts())
    print("合格统计：")
    print("总数：" + str(good_water_sum) + " 合格：" +
          str(expected_water_count[1]) + " 否：" + str(expected_water_count[0]))
    expected_water_scale = round(
        (expected_water_count[1] / good_water_sum), 3)
    print("合格比例：" + str(expected_water_scale))

    # 未达标统计below quality
    below_quality_sites = good_water_df[good_water_df["合格"] == 0]
    below_quality_name = ""
    for index, row in below_quality_sites.iterrows():
        below_quality_name += row["水体名称"] + row["测点名称"] + "、"
    below_quality_num = str(expected_water_count[0])
    print("未达标断面数：" + below_quality_num)
    below_quality_name_str = below_quality_name[:-1]
    print("未达标断面名称：" + below_quality_name_str)
    print("---------------------------------------------------")
    seq = "\n"
    result = "****************************************************" + seq
    result += "优Ⅲ统计：" + seq 
    result += "总数：" + str(good_water_sum) + " 优Ⅲ：" + str(good_water_count[1]) + " 否：" + str(good_water_count[0]) + seq
    result += "优Ⅲ比例：" + str(good_water_scale) + seq
    result += "---------------------------------------------------" + seq
    result += "合格统计：" + seq
    result += "总数：" + str(good_water_sum) + " 合格：" + str(expected_water_count[1]) + " 否：" + str(expected_water_count[0]) + seq
    result += "合格比例：" + str(expected_water_scale) + seq
    result += "未达标断面数：" + below_quality_num + seq
    result += "未达标断面名称：" + below_quality_name_str + seq
    result += "---------------------------------------------------" + seq

    with open(file_name, "a") as file:
        file.write(result)
        file.close()


def main_oneFile(name):
    # 遍历文件中的sheet
    f = pd.ExcelFile(source_url + os.sep + name)
    # 获取工作表名称
    f.sheet_names

    for i in f.sheet_names:
        countryFlag = 0
        file_sheet = pd.read_excel(source_url + os.sep + name, sheet_name=i)
        for column_name in list(file_sheet):
            if column_name == "前五项水质类别":
                countryFlag = 1

        if countryFlag == 1:
            # 国考流程
            main_countryFile(file_sheet, i)
        else:
            # 省考流程
            main_provinceFile(file_sheet, i)

# 程序入口
ls = os.listdir(target_url + os.sep)
for i in ls:
    c_path = os.path.join(target_url + os.sep, i)
    os.remove(c_path)

for root, dirs, files in os.walk(source_url):
    for name in files:
        main_oneFile(name)
