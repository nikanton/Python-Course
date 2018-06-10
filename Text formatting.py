l = 40;
p = 10;
ans = ''
letters = 0;
with open('input.txt') as f:
    words = []
    new_paragraph = True;
    for i in f:
        if i == '\n':
            new_paragraph = True;
        else:
            words = i.rstrip('\n').split(' ')
            for j in range(words.count('')):
                words.remove('')
            if new_paragraph:
                ans = ans.rstrip(' ')
                if ans != '':
                    ans += '\n'
                for i in range(p):
                    ans += ' '
                letters = p;
                ans += words[0]  + ' '
                letters += len(words[0]) + 1
                if letters > l + 1:
                    raise ValueError('Too long word: ' + words[0] + '\n' + str(len(words[0])) + ' letters');
                words.remove(words[0])
            for i in words:
                if len(i) > l:
                    raise ValueError('Too long word: ' + i + '\n' + str(len(i)) + ' letters');
                if letters + len(i) <= l:
                    ans += i  + ' '
                    letters += len(i) + 1
                else:
                    ans = ans.rstrip(' ')
                    ans += '\n' + i + ' '
                    letters = len(i) + 1 

ans = ans.rstrip(' ')
print ans