from facebook_scraper import get_posts
import re

############################################################################################################
# Get post fucntions access the post. get_posts fucntion accepts different kind of arguments which can
# be post_URLs in form of list, account_id or group id. Here after accessing the post by link. The comments
# are stored in list called comments. After that comments are sent to function called extract phone numbers
############################################################################################################https://www.facebook.com/PatriceTalon.PR/posts/772846929487633  
def getPost():
 for post in get_posts(post_urls=["https://www.facebook.com/polioeradicationinitiative/posts/3041220072757022"], options={"reactors": True}, timeout=100):
     print("User Name                 "+ str(post['username']))
     print("Total Number of comments  "+ str(post['comments']))
     print("Total Number of likes     "+ str(post['likes']))
     print("Total Number of reactions "+ str(post['reactions']))
     print("Total Number of shares    "+ str(post['shares']))
     print(str(post['text']))
 #extractPhoneNumber(comments)
if __name__ == '__main__':
    getPost()
