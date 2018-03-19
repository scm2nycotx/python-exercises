def banner(text, ch="*", length=78):
    if text is None:
        return ch * length
    elif len(text) + 2 + len(ch) * 2 > length:
        return text
    else:
        remain = length - (len(text) + 2)
        prefix_len = remain / 2
        suffix_len = remain - prefix_len
        if len(ch) == 1:
            prefix = ch * int(prefix_len)
            suffix = ch * int(suffix_len)
        else:
            prefix = ch * int((prefix_len / len(ch))) + ch[:prefix_len % len(ch)]
            suffix = ch * int((suffix_len / len(ch))) + ch[:suffix_len % len(ch)]
        return prefix + " " + text + suffix

