import praw
import random
import datetime
import nltk
from textblob import TextBlob
from dateutil.relativedelta import relativedelta
import lab

# FIXME:
# copy your generate_comment functions from the week_07 lab here

# connect to reddit 
reddit = praw.Reddit('bot')

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040/comments/j9vb5b/the_2020_election_bot_debate_thread/'
submission = reddit.submission(url=reddit_debate_url)
my_candidate1 = 'sherlock'
my_candidate2 = "sherlock holmes"
my_candidate3 = 'dr strange'
my_candidate4 = 'dr. strange'
my_candidate5 = 'benedict cumberbatch'
other_candidate = 'superman'
my_account = 'sarah_bot'
subreddit_favoring = 'BenedictCumberbatch'



# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:
    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

   

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    all_comments = []
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        all_comments.append(comment)
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if comment.author != my_account:
            not_my_comments.append(comment)

    ###################################### EXTRA CREDIT: UPVOTE COMMENT IF CANDIDATE MENTIONED ######################################
    for comment in not_my_comments:
        if my_candidate1.lower() in comment.body.lower() and my_candidate2.lower() in comment.body.lower() and my_candidate3.lower() in comment.body.lower() and my_candidate4.lower() in comment.body.lower() and my_candidate5.lower() in comment.body.lower():
            comment.upvote()
    
    ###################################### EXTRA CREDIT: UPVOTE/DOWNVOTE COMMENT/SUBMISSION IF BASED ON SENTIMENT ON CANDIDATE ######################################
    #sentiment for my candidate
    for comment in not_my_comments:
        if my_candidate1.lower() in comment.body.lower() and my_candidate2.lower() in comment.body.lower() and my_candidate3.lower() in comment.body.lower() and my_candidate4.lower() in comment.body.lower() and my_candidate5.lower() in comment.body.lower():
            if TextBlob(comment.body).sentiment.polarity > 0:
                comment.upvote()
            elif TextBlob(comment.body).sentiment.polarity < 0:
                comment.downvote()
    for sub in reddit.subreddit("csci040").new(limit=None):
        if my_candidate1.lower() in sub.title.lower() and my_candidate2.lower() in sub.title.lower() and my_candidate3.lower() in sub.title.lower() and my_candidate4.lower() in sub.title.lower() and my_candidate5.lower() in sub.title.lower():
            if TextBlob(sub.title).sentiment.polarity > 0:
                sub.upvote()
            elif TextBlob(sub.title).sentiment.polarity < 0:
                sub.downvote()
    #sentiment for opposing candidate
    for comment in not_my_comments:
        if other_candidate.lower() in comment.body.lower():
            if TextBlob(comment.body).sentiment.polarity > 0:
                comment.downvote()
            elif TextBlob(comment.body).sentiment.polarity < 0:
                comment.upvote()
    for sub in reddit.subreddit("csci040").new(limit=None):
        if other_candidate.lower() in comment.body.lower():
            if TextBlob(sub.title).sentiment.polarity > 0:
                sub.downvote()
            elif TextBlob(sub.title).sentiment.polarity < 0:
                sub.upvote()
              

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit

        generated = lab.generate_comment()
        submission.reply(generated)
    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over has_not_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            have_replied = False
            for replies in comment.replies:
                if replies.author is None:
                    have_replied = True
                if replies.author is not None:
                    if replies.author == my_account:
                        have_replied = True
            if not have_replied and comment.author is not None:
                comments_without_replies.append(comment)
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit\

        # Task 4 commented since I reply to upvoted comments first
        #to_reply = random.choice(comments_without_replies_list)
        #generated = lab.generate_comment()
        #to_reply.reply(generated)
        ###################################### EXTRA CREDIT: REPLY TO HIGH UPVOTED COMMENTS BEFORE ######################################
        comments_without_replies = sorted(comments_without_replies,key = lambda x: x.score)
        generated = lab.generate_comment()
        to_reply = comments_without_replies[len(comments_without_replies)-1]
        to_reply.reply(generated)

    ###################################### EXTRA CREDIT: UPVOTE SUBMISSION IF CANDIDATE MENTIONED ######################################
    subreddit  = reddit.subreddit("csci040")
    for sub in subreddit.new(limit=None):
        if my_candidate1.lower() in sub.title.lower() and my_candidate2.lower() in sub.title.lower() and my_candidate3.lower() in sub.title.lower() and my_candidate4.lower() in sub.title.lower() and my_candidate5.lower() in sub.title.lower():
            sub.upvote()

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions
    probability = random.random()
    if probability < 0.5:
        submission = reddit.submission(url=reddit_debate_url)
    else:
        top_last_month = []
        for sub in subreddit.top("all"):
            submission_date = datetime.datetime.fromtimestamp(sub.created_utc)
            amonth_ago = datetime.datetime.now() - relativedelta(months=1)
            if submission_date > amonth_ago:
                top_last_month.append(sub)
        submission = random.choice(top_last_month)
