def cipher(sent):
    alph = {65:"a", 66:"b", 67:"c", 68:"d", 69:"e", 70:"f", 71:"g", 72:"h", 73:"i", 74:"j", 75:"k", 76:"l", 77:"m", 78:"n", 79:"o", 80:"p", 81:"q", 82:"r", 83:"s", 84:"t", 85:"u", 86:"v", 87:"w", 88:"x", 89:"y", 90:"z"}
    order = 65
    for i in alph:
        sent = sent.replace(alph[i], str(i))
        order += 1
    print(sent)
sent = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
cipher(sent)