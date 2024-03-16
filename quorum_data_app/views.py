from django.shortcuts import render
import csv

def index(request):
    return render(request, 'index.html')

def get_legislator_bills_info(request):
    # Get information about legislators and the bills they supported/opposed.
    legislators_data = process_legislators('dataset/legislators_(2).csv')
    return render(request, 'legislator_info.html', {'legislators_data': legislators_data})

def get_bill_legislators_info(request):
    # Get information about bills and the legislators who supported/opposed them.
    bills_data = process_bills('dataset/bills_(2).csv')
    return render(request, 'bill_info.html', {'bills_data': bills_data})


def process_legislators(csv_file):
    # Process legislators' data.
    legislators = {}
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            legislator_id = row['id']
            if legislator_id not in legislators:
                legislators[legislator_id] = {'name': row['name'], 'supported_bills': 0, 'opposed_bills': 0}

    # Process legislators' votes on each bill.
    with open('dataset/vote_results_(2).csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            legislator_id = row['legislator_id']
            vote_type = int(row['vote_type'])
            if vote_type == 1:
                legislators[legislator_id]['supported_bills'] += 1
            elif vote_type == 2:
                legislators[legislator_id]['opposed_bills'] += 1

    return legislators


def process_bills(csv_file):
    # Process bills' data.
    bills = {}
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bill_id = row['id']
            if bill_id not in bills:
                bills[bill_id] = {'title': row['title'], 'supported_legislators': 0, 'opposed_legislators': 0,
                                  'primary_sponsor': row['sponsor_id']}

    # Process vote types and find the bill.
    votes = {}
    with open('dataset/votes_(2).csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vote_id = row['id']
            if vote_id not in votes:
                votes[vote_id] = {'bill_id': row['bill_id']}

    # Process legislators' votes on each bill.
    with open('dataset/vote_results_(2).csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vote_id = row['vote_id']
            bill_id = votes[vote_id]['bill_id']
            vote_type = int(row['vote_type'])
            if vote_type == 1:
                bills[bill_id]['supported_legislators'] += 1
            elif vote_type == 2:
                bills[bill_id]['opposed_legislators'] += 1

    return bills
