TV_plays=[('《Give up，hold on to me》',1.4),
          ('《The private dishes of the husbands》',1.343),
          ('《My father-in-law will do martiaiarts》',0.92),
          ('《North Canton still believe in love》',0.862),
          ('《Impossible task》',0.553),
          ('《Sparrow》',0.411),
          ('《East of dream Avenue》',0.164),
          ('《Theprodigal son of the new frontier town》',0.259),
          ('《Distant distance》',0.394),
          ('《Music legend》',0.562),
          ]
TV_plays = {
1.4:'《Give up，hold on to me》',
1.343:'《The private dishes of the husbands》',
0.92:'《My father-in-law will do martiaiarts》',
0.862:'《North Canton still believe in love》',
0.553:'《Impossible task》',
0.411:'《Sparrow》'
}
TV_plays_list = [1.4,1.343,0.92,0.862,0.553,0.411]
TV_plays_list1 = sorted(TV_plays_list)
new_list = []
for item in TV_plays_list1:
    new_list.append((item,TV_plays[item]))
print(new_list)