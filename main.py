import json
import time
import csv

# Open the file for reading (replace 'file.json' with your filename)
with open('reviews.json', 'r') as f:
    # Use the json module to load the data
    data = json.load(f)
    total_reviews = 0
    all_reviews_dump = data
    clean_reviews = [["Date", "Rating (1-5)", "Name", "Review", "Top Reply"]]
    for review_page in all_reviews_dump:
        page_reviews = review_page[0][1][4]
        clean_page_reviews = []
        for r in page_reviews:
            total_reviews += 1
            text = r[4]
            rating = r[3]
            epoch_ms = r[6]
            readable_time = time.strftime('%d-%m-%Y', time.gmtime(epoch_ms/1000.0))
            rater_name = r[2][1]
            comment_text = ""
            if len(r[9]) > 5:
                reviewer_name = r[9][4][0][2][1]
                reviewer_text = r[9][4][0][4]
                comment_text = "By "+reviewer_name+" | Comment: "+reviewer_text
            clean_page_reviews.append([readable_time,rating,rater_name,text,comment_text])
        clean_reviews = clean_reviews + clean_page_reviews
    print("Reviews Extracted - {}".format(total_reviews))
    filename = "reviews.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)

        # Write the data
        for row in clean_reviews:
            writer.writerow(row)
        print("Process Done! Saved in {}".format(filename))
    