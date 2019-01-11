#! /usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import json
import numpy as np
import pandas as pd

def Evaluate(commit_data, judge_data):
    """
    compute score according to competition
    """
    # commit_data = commit_data[commit_data["ID"].isin(judge_data["ID"].values)]
    mean_values = (commit_data == judge_data).mean(axis = 1).values
    score = (mean_values < 1).mean()
    return score


def Check_evaluate(userCommitFile, judgeAFile, judgeBFile = None, aOrB = None):
    result = {}
    """
    check userCommitFile, judgeAFile, judgeBFile
    """
    if userCommitFile is None or judgeAFile is None or (aOrB is not None and judgeBFile is None):
       result["status"] = False
       # result["msg"] = "参数错误"
       result["msg"] = "parameter error" 
       print(json.dumps(result)) 
       exit() 

    """ 
    check aOrB 
    """ 
    if aOrB is not None and aOrB != "a" and aOrB != "b":
       result["status"] = False
       # result["msg"] = "参数aOrB错误"
       result["msg"] = "parameter aOrB error"
       print(json.dumps(result))
       exit()


    if aOrB is not None:
        """
        loading data
        """
        try:
            commit_data = pd.read_csv(userCommitFile, encoding = "gbk")
            judge_data_a = pd.read_csv(judgeAFile, encoding = "gbk")
            judge_data_b = pd.read_csv(judgeBFile, encoding = "gbk")
        except:
            result["status"] = False
            # result["msg"] = "文件地址错误"
            result["msg"] = "file address error"
            print(json.dumps(result))
            exit()
        
        """
        check shape of commit data
        """
#        if commit_data.shape[0] != judge_data_a.shape[0] + judge_data_b.shape[0]:
#            result["status"] = False
#            # result["msg"] = "行数错误"
#            result["msg"] = "num_lines error"
#            print(json.dumps(result))
#            exit()
#        if commit_data.shape[1] != judge_data_a.shape[1] + judge_data_b.shape[1]:
#            result["status"] = False
#            # result["msg"] = "列数错误"
#            result["msg"] = "num_columns error"
#            print(json.dumps(result))
#            exit()
        
        """
        check columns and index
        """
        if (commit_data.columns.values == judge_data_a.columns.values).mean() < 1:
            result["status"] = False
            # result["msg"] = "列名错误"
            result["msg"] = "column name error"
            print(json.dumps(result))
            exit()     

        """
        check max and min values
        """
        if commit_data.max().max() > sys.maxsize or commit_data.min().min() < -sys.maxsize - 1:
            result["status"] = False
            # result["msg"] = "数值越界错误"
            result["msg"] = "number out of bounds"
            print(json.dumps(result))
            exit()

        """
        check nan
        """
#        if commit_data.mean().mean() != 0:
#            result["status"] = False
#            # result["msg"] = "空值错误"
#            result["msg"] = "nan error"
#            print(json.dumps(result))
#            exit()

        """
        check dtype
        """
        for i in range(commit_data.shape[1]):
            if commit_data.iloc[:, i].dtype != judge_data_a.iloc[:, i].dtype:
                result["status"] = False
                # result["msg"] = str(i) + "列类型错误"
                result["msg"] = str(i) + "column type error"
                print(json.dumps(result))
                exit()

        """
        check id
        """
#        equal_array = (np.sort(commit_data["ID"].values) ==  \
#        np.sort(np.concatenate([judge_data_a["ID"].values, judge_data_a["ID"].values], axis = 0)))
#        if equal_array.mean() != 0:
#            result["status"] = False
#            # result["msg"] = "ID错误"
#            result["msg"] = "ID error"
#            print(json.dumps(result))
#            exit()

        """
        compute score
        """
        if aOrB == "a":
            score = Evaluate(commit_data, judge_data_a)
            result["status"] = True
            # result["msg"] = "没有错误"
            result["msg"] = "no error"
            result["data"] = {0: score}
            print(json.dumps(result))
        else:
            score = Evaluate(commit_data, judge_data_b)
            result["status"] = True
            # result["msg"] = "没有错误"
            result["msg"] = "no error"
            result["data"] = {0: score}
            print(json.dumps(result))
    else:
        """
        load data
        """
        try:
            commit_data = pd.read_csv(userCommitFile, encoding = "gbk")
            judge_data = pd.read_csv(judgeAFile, encoding = "gbk")
        except:
            result["status"] = False
            result["msg"] = "parameter error"
            print(json.dumps(result))
            exit()

        """
        check shape of commit_data
        """
        if commit_data.shape[0] != judge_data.shape[0]:
            result["status"] = False
            result["msg"] = "num_rows error"
            print(json.dumps(result))
            exit()
        if commit_data.shape[1] != judge_data.shape[1]:
            result["status"] = False
            result["msg"] = "num_columns error"
            print(json.dumps(result))
            exit()

        """
        check columns and index
        """
        if (commit_data.columns.values == judge_data.columns.values).mean() < 1:
            result["status"] = False
            # result["msg"] = "列名错误"
            result["msg"] = "column name error"
            print(json.dumps(result))
            exit()     

        """
        check max and min values
        """
        if commit_data.max().max() > sys.maxsize or commit_data.min().min() < -sys.maxsize - 1:
            result["status"] = False
            # result["msg"] = "数值越界错误"
            result["msg"] = "number out of bounds"
            print(json.dumps(result))
            exit()

        """
        check nan
        """
#        if commit_data.mean().mean() != 0:
#            result["status"] = False
#            # result["msg"] = "空值错误"
#            result["msg"] = "nan error"
#            print(json.dumps(result))
#            exit()
        
        """
        check dtype
        """
        for i in range(commit_data.shape[1]):
            if commit_data.iloc[:, i].dtype != judge_data.iloc[:, i].dtype:
                result["status"] = False
                # result["msg"] = str(i) + "列类型错误"
                result["msg"] = str(i) + "column type error"
                print(json.dumps(result))
                exit()
        
        """
        check id
        """
#        equal_array = (np.sort(commit_data["ID"].values) ==  \
#        np.sort(judge_data["ID"].values))
#        if equal_array.mean() != 0:
#            result["status"] = False
#            # result["msg"] = "ID错误"
#            result["msg"] = "ID error"
#            print(json.dumps(result))
#            exit()
        
        """
        compute score
        """
        score = Evaluate(commit_data, judge_data)
        result["status"] = True
        # result["msg"] = "没有错误"
        result["msg"] = "no error"
        result["data"] = {0: score}
        print(json.dumps(result))

if __name__ == "__main__":
    num_argvs = len(sys.argv) - 1
    if num_argvs == 2:
        Check_evaluate(sys.argv[1], sys.argv[2])
    elif num_argvs == 4:
        Check_evaluate(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        result = {}
        result["status"] = False
        # result["msg"] = "参数数量错误"
        result["msg"] = "num_argvs error"
        print(json.dumps(result))
        exit()
