#TASK 3

#Note: I have only worked on Step 1 and started Step 2. 

#import libraries
import pandas as pd
import numpy as np
import json

#STEP 1------------------------------------------------------------------------------------------------------------------------------------
#read json file
with open("following.json") as followingData:
   followingList= json.load(followingData)

# Note: The "following.json" file is a list of dictionaries
# For each dictionary in the list, "follower_uid" is the key to access the value, which is the follower_user_id (let's call this followerId)
# For each dictionary in the list, "influencer_uid" is the key to access the value, which is the influencer_user_id (let's call this influencerId)
# I want to make a function that takes in all dictionaries in the list and makes the influencerId the key, and the followerId the value
def merge_dicts_following(followingList):
    followingDict = {}
    for dictionary in followingList:
        influencerId = dictionary["influencer_uid"]
        followerId = dictionary["follower_uid"]
        followingDict.setdefault(influencerId, []).append(followerId)
    return followingDict

merged_dict_following = merge_dicts_following(followingList)

#For any pair of influencerId (keys) in the dictionary, I want to:
    #Compare their lists of followerId (values)
    #Use an existing function to compare the two lists and return matches
    #Use a function to count the number of matches
    #Use a function to count the number of followerId in each of the two lists 
    #See which of the two lists is smaller (have less followers)
    #Divide the number of matches over the number of followeId in the smaller list

#Example variables of 2 influencers' user ID's:
influencerId1 = "902200087"
influencerId2 = "969221141347913734"

list1 = merged_dict_following.get(influencerId1, [])
list2 = merged_dict_following.get(influencerId2, [])

#function: return matches
def compare_lists(list1, list2):
    matches = list(set(list1) & set(list2))
    return matches

#print matches 
matches = compare_lists(list1, list2)
print ("These are the IDs of the shared followers between the influencers",influencerId1, "and", influencerId2, ": ", matches)

#function: count matches
def count_matches(matches):
    return len(matches)

#function: count followers 
def count_followers(follower_list):
    return len(follower_list)

#function: calculate match ratio 
def calculate_match_ratio(json_data):
    result_dict = {}
    for item in json_data:
        influencer_id = item['influencer_uid']
        follower_id = item['follower_uid']
        result_dict.setdefault(influencer_id, []).append(follower_id)

    for influencerId1, list1 in result_dict.items():
        for influencerId2, list2 in result_dict.items():
            if influencerId1 != influencerId2:
                #count the number of followers the influencers share
                matches = compare_lists(list1, list2)
                match_count = count_matches(matches)
                #count the number of followers that each influencer has
                follower_count1 = count_followers(list1)
                follower_count2 = count_followers(list2)
                #determine the smaller list of followers
                smaller_list_count = min(follower_count1, follower_count2)
                
                #calculate match ratio
                match_ratio = match_count / smaller_list_count if smaller_list_count > 0 else 0

    return match_ratio

#print match ratio
match_ratio = calculate_match_ratio(followingList)
print("The fraction of followers these two influencers share over the total number of followers of the less followed influencer is: ", match_ratio)


#STEP 2------------------------------------------------------------------------------------------------------------------------------------
#Read json file
with open("engagement.json") as engagementData:
   engagementList= json.load(engagementData)

#The "engagement.json" file is a list of dictionaries, just like the "following.json" file
# I want to make a function that takes in all dictionaries in the list and makes the influencer_id the key
# The follower_id, engaged_tweet_id, and date_time will be the values
def merge_dicts_engagement(engagementList):
    engagementDict = {}
    for dictionary in engagementList:
        influencer_id = dictionary["influencer_uid"]
        follower_id  = dictionary["follower_uid"]
        engaged_tweet_id  = dictionary["engaged_tweetID"]
        date_time = dictionary["engaged_dt"]

        if influencer_id  not in engagementDict:
            engagementDict[influencer_id ] = []

#Note: The below code does not work.................................
#         engagementList[influencer_id].append({
#             "followerId": follower_id,
#             "engagedTweetId": engaged_tweet_id,
#             "dateTime": date_time
#             })
#     return engagementDict


# merged_dict_engagement = merge_dicts_engagement(engagementList)
# print (merged_dict_engagement[1298372735383605249])