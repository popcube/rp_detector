# RP_DETECTOR  
This Python script shows the datetime and alt url of repost on someone's X individual timeline.  
As is often the case with X, the data scheme changes without notice so there is no guarantee that the script works after the release of the script, Sep 1st 2024.  

- Validated on Python 3.10.4
- Only standard libraries required
- Generate csv file

## How to use

1. open browser tab on PC
2. press F12 and open developer console
3. in the Filter form under Network tab, type "userTweets" (without quotes)
4. move to someone's X home in the same browser tab
   e.g. https://x.com/elonmusk
5. click one entry that starts with userTweets that appeared in Name section  
6. move to Response tab
7. copy the text and save as userTweet.json on your local directory
9. execute repost_detector.py on the same directory

EXAMPLE

---

|RP_DATE                  |RP_URL                                           |ORG_DATE                 |ORG_URL                                                |
|-------------------------|-------------------------------------------------|-------------------------|-------------------------------------------------------|
|2024-08-25T11:17:31+00:00|https://x.com/elonmusk/status/1827666612423422302|2024-08-24T15:54:11+00:00|https://x.com/iamyesyouareno/status/1827373851639996482|
|2024-08-25T11:08:53+00:00|https://x.com/elonmusk/status/1827664438192685415|2024-08-23T19:10:36+00:00|https://x.com/TheChiefNerd/status/1827060893630497040  |
|2024-08-25T11:03:15+00:00|https://x.com/elonmusk/status/1827663021226741971|2024-08-25T10:53:53+00:00|https://x.com/elon_docs/status/1827660664074055837     |
|2024-08-25T10:48:53+00:00|https://x.com/elonmusk/status/1827659408702062997|2024-08-25T10:44:14+00:00|https://x.com/chrispavlovski/status/1827658235618144257|
|2024-08-25T10:30:49+00:00|https://x.com/elonmusk/status/1827654859618693496|2024-08-24T13:45:02+00:00|https://x.com/IEA/status/1827341347881132206           |
|2024-08-25T10:27:28+00:00|https://x.com/elonmusk/status/1827654017117462885|2024-08-25T00:37:44+00:00|https://x.com/Geiger_Capital/status/1827505606539772223|
|2024-08-25T10:20:24+00:00|https://x.com/elonmusk/status/1827652239722258783|2024-08-24T17:15:55+00:00|https://x.com/BillboardChris/status/1827394420448362935|
|2024-08-25T10:18:53+00:00|https://x.com/elonmusk/status/1827651854978744506|2024-08-24T15:05:23+00:00|https://x.com/SawyerMerritt/status/1827361568192934054 |

