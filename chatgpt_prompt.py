import helper
from dotenv import load_dotenv,find_dotenv
_ = load_dotenv(find_dotenv())

#result = helper.get_completion("Explain mutual funds in simple terms")
###########################
###propmt one example##
text = """You should express what you want a model to do by  
providing instructions that are as clear and  
specific as you can possibly make them. 
This will guide the model towards the desired output,
and reduce the chances of receiving irrelevant
or incorrect responses. Don't confuse writing a 
clear prompt with writing a short prompt.
In many cases, longer prompts provide more clarity
and context for the model, which can lead to
more detailed and relevant outputs."""

prompt = f"""Summarize the text delimited by triple backticks  
into a single sentence ```{text}```"""

result = helper.get_completion(prompt)
#print(result)

###############

prompt = """Generate list of fruits with name,available in which season and approx market price give output in json format"""
result = helper.get_completion(prompt)
#print(result)

##############

text_2 = """
The sun is shining brightly today, and the birds are 
singing. It's a beautiful day to go for a
walk in the park. The flowers are blooming, and the
trees are swaying gently in the breeze. People 
are out and about, enjoying the lovely weather. 
Some are having picnics, while others are playing 
games or simply relaxing on the grass. It's a
perfect day to spend time outdoors and appreciate the
beauty of nature.
"""
prompt = """
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions,
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, 
then simply write "No steps provided."

{text_2}
"""
response = helper.get_completion(prompt)
#print("Completion for Text 2:")
#print(response)

############

text_1 = """
Making a cup of tea is easy! First, you need to get some 
water boiling. While that's happening, 
grab a cup and put a tea bag in it. Once the water is
hot enough, just pour it over the tea bag.
Let it sit for a bit so the tea can steep. After a
few minutes, take out the tea bag. If you
like, you can add some sugar or milk to taste. 
And that's it! You've got yourself a delicious 
cup of tea to enjoy.
"""
prompt = """
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions,
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, 
then simply write \"No steps provided.\"

{text_1}
"""
response = helper.get_completion(prompt)
#print("Completion for Text 1:")
#print(response)

###########
text = """
In a charming village, siblings Jack and Jill set out on 
a quest to fetch water from a hilltop 
well. As they climbed, singing joyfully, misfortune
struck—Jack tripped on a stone and tumbled
down the hill, with Jill following suit. 
Though slightly battered, the pair returned home to 
comforting embraces. Despite the mishap,
their adventurous spirits remained undimmed, and they
continued exploring with delight.
"""

prompt2 = """Your task is to perform below actions
1.Summarize the following text delimited by 
  <> into 1 sentence
2.Translate summary in marathi
3.Generate output in json format in format of key marathi_summary,num_names 
{text}
"""

response = helper.get_completion(prompt2)
#print("Completion for prompt 1:")
#print(response)
################
prompt = """
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
"""
response = helper.get_completion(prompt)
#print(response)
####

fact_sheet_chair = """
OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture, 
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100) 
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black, 
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities: 
 medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests 

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy
"""

prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.


At the end of the description, include every 7-character 
Product ID in the technical specification.

Use at most 50 words.

Technical specifications: ```{fact_sheet_chair}```
"""

response = helper.get_completion(prompt)
#print(response)

######
prod_review = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and 
super cute, and its face has a friendly look. It's 
a bit small for what I paid though. I think there 
might be other options that are bigger for the 
same price. It arrived a day earlier than expected,  
so I got to play with it myself before I gave it  
to her.
"""

prompt = f"""
Your task is to extract relevant information from 
a product review from an ecommerce site to give
feedback to the Shipping department. 

From the review below,extract the information relevant to shipping and 
delivery. Limit to 30 words. 

{prod_review}
"""

response = helper.get_completion(prompt)
##print(response)

#########

review_1 = prod_review 

# review for a standing lamp
review_2 = """
Needed a nice lamp for my bedroom, and this one \
had additional storage and not too high of a price \
point. Got it fast - arrived in 2 days. The string \
to the lamp broke during the transit and the company \
happily sent over a new one. Came within a few days \
as well. It was easy to put together. Then I had a \
missing part, so I contacted their support and they \
very quickly got me the missing piece! Seems to me \
to be a great company that cares about their customers \
and products. 
"""

# review for an electric toothbrush
review_3 = """
My dental hygienist recommended an electric toothbrush, \
which is why I got this. The battery life seems to be \
pretty impressive so far. After initial charging and \
leaving the charger plugged in for the first week to \
condition the battery, I've unplugged the charger and \
been using it for twice daily brushing for the last \
3 weeks all on the same charge. But the toothbrush head \
is too small. I’ve seen baby toothbrushes bigger than \
this one. I wish the head was bigger with different \
length bristles to get between teeth better because \
this one doesn’t.  Overall if you can get this one \
around the $50 mark, it's a good deal. The manufactuer's \
replacements heads are pretty expensive, but you can \
get generic ones that're more reasonably priced. This \
toothbrush makes me feel like I've been to the dentist \
every day. My teeth feel sparkly clean! 
"""

# review for a blender
review_4 = """
So, they still had the 17 piece system on seasonal \
sale for around $49 in the month of November, about \
half off, but for some reason (call it price gouging) \
around the second week of December the prices all went \
up to about anywhere from between $70-$89 for the same \
system. And the 11 piece system went up around $10 or \
so in price also from the earlier sale price of $29. \
So it looks okay, but if you look at the base, the part \
where the blade locks into place doesn’t look as good \
as in previous editions from a few years ago, but I \
plan to be very gentle with it (example, I crush \
very hard items like beans, ice, rice, etc. in the \ 
blender first then pulverize them in the serving size \
I want in the blender then switch to the whipping \
blade for a finer flour, and use the cross cutting blade \
first when making smoothies, then use the flat blade \
if I need them finer/less pulpy). Special tip when making \
smoothies, finely cut and freeze the fruits and \
vegetables (if using spinach-lightly stew soften the \ 
spinach then freeze until ready for use-and if making \
sorbet, use a small to medium sized food processor) \ 
that you plan to use that way you can avoid adding so \
much ice if at all-when making your smoothie. \
After about a year, the motor was making a funny noise. \
I called customer service but the warranty expired \
already, so I had to buy another one. FYI: The overall \
quality has gone done in these types of products, so \
they are kind of counting on brand recognition and \
consumer loyalty to maintain sales. Got it in about \
two days.
"""

reviews = [review_1, review_2, review_3, review_4]

for i in range(len(reviews)):
    prompt = f"""
    Your task is to generate a short summary of a product
    review from an ecommerce site. 

    Summarize the review below,in at most 20 words. 
       {reviews[i]}"""
    
    result = helper.get_completion(prompt)
    #print(result)

    ######
    lamp_review = """
Needed a nice lamp for my bedroom, and this one had 
additional storage and not too high of a price point. 
Got it fast.  The string to our lamp broke during the 
transit and the company happily sent over a new one 
Came within a few days as well. It was easy to put 
together.  I had a missing part, so I contacted their 
support and they very quickly got me the missing piece! 
Lumina seems to me to be a great company that cares 
about their customers and products!!
"""

prompt = f"""
Identify the following items from the review text: 
- Sentiment (positive or negative)
- Is the reviewer expressing anger? (true or false)
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks. 
Format your response as a JSON object with 
"Sentiment", "Anger", "Item" and "Brand" as the keys.
If the information isn't present, use "unknown" 
as the value.
Make your response as short as possible.
Format the Anger value as a boolean.

{lamp_review}
"""
response = helper.get_completion(prompt)
#print(response)

####

sentiment = "negative"

# review for a blender
review = f"""
So, they still had the 17 piece system on seasonal 
sale for around $49 in the month of November, about 
half off, but for some reason (call it price gouging) 
around the second week of December the prices all went 
up to about anywhere from between $70-$89 for the same 
system. And the 11 piece system went up around $10 or 
so in price also from the earlier sale price of $29. 
So it looks okay, but if you look at the base, the part 
where the blade locks into place doesn’t look as good 
as in previous editions from a few years ago, but I 
plan to be very gentle with it (example, I crush 
very hard items like beans, ice, rice, etc. in the  
blender first then pulverize them in the serving size 
I want in the blender then switch to the whipping 
blade for a finer flour, and use the cross cutting blade 
first when making smoothies, then use the flat blade 
if I need them finer/less pulpy). Special tip when making 
smoothies, finely cut and freeze the fruits and 
vegetables (if using spinach-lightly stew soften the  
spinach then freeze until ready for use-and if making 
sorbet, use a small to medium sized food processor)  
that you plan to use that way you can avoid adding so 
much ice if at all-when making your smoothie. 
After about a year, the motor was making a funny noise. 
I called customer service but the warranty expired 
already, so I had to buy another one. FYI: The overall 
quality has gone done in these types of products, so 
they are kind of counting on brand recognition and 
consumer loyalty to maintain sales. Got it in about 
two days.
"""


prompt = f"""
You are a customer service AI assistant.
Your task is to send an email reply to a valued customer.
Given the customer email delimited by ```,
Generate a reply to thank the customer for their review.
If the sentiment is positive or neutral, thank them for 
their review.
If the sentiment is negative, apologize and suggest that 
they can reach out to customer service. 
Make sure to use specific details from the review.
Write in a concise and professional tone.
Sign the email as `AI customer agent`.
Customer review: ```{review}```
Review sentiment: {sentiment}
"""
response = helper.get_completion(prompt,temp=0.7)
print(response)