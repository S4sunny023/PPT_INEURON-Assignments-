def compress(chars):
    readPtr = writePtr = 0
    count = 1

    for i in range(1, len(chars)):
        if chars[i] == chars[i-1]:
            count += 1
        else:
            chars[writePtr] = chars[readPtr]
            writePtr += 1

            if count > 1:
                countStr = str(count)
                for j in range(len(countStr)):
                    chars[writePtr] = countStr[j]
                    writePtr += 1

            count = 1
            readPtr = i

    chars[writePtr] = chars[readPtr]
    writePtr += 1

    if count > 1:
        countStr = str(count)
        for j in range(len(countStr)):
            chars[writePtr] = countStr[j]
            writePtr += 1

    return writePtr

# Test the code
chars = ["a","a","b","b","c","c","c"]
newLength = compress(chars)
print(newLength)
print(chars[:newLength])
