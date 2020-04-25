from django.shortcuts import render

from text.cipherMessage import (
    encryption,
    keycodeParser,
)

from text.formatTabIndent import (
    formatter,
)

from text.generatePassword import (
    characterGroup,
    characterLength,
)

# Create your views here.

def text(request):
    template = "text/text.html"
    context = {}
    return render(request, template, context)

def cipherMessage(request):
    template = "text/cipherMessage.html"
    context = {}

    if request.method == "POST":
        keycode = request.POST.get("keycode", "")
        textToCipher = request.POST.get("textToCipher", "")
        keycodeDifferences = keycodeParser.getDifferencesBetweenChars(keycode)
        print(keycodeDifferences)

        encryptedText = encryption.encrypt(textToCipher, keycodeDifferences)
        print(encryptedText)

    return render(request, template, context)

def formatTabIndent(request):
    template = "text/formatTabIndent.html"
    context = {
        "tabMultiplier" : formatter.DEFAULT_TAB_INDENT_MULTIPLIER
    }

    if request.method == "POST":
        tabMultiplier = request.POST.get("tabMultiplier", "")
        textToFormat = request.POST.get("textToFormat", "")
        formattedText = formatter.formatTab(tabMultiplier, textToFormat)

        context["tabMultiplier"] = tabMultiplier
        context["textToFormat"] = textToFormat
        context["formattedText"] = formattedText

    return render(request, template, context)

def generatePassword(request):
    template = "text/generatePassword.html"
    context = {}

    if request.method == "POST":
        groups = characterGroup.getCharacterGroups()
        characterGroup.shuffleCharacterGroups(groups)
        targetLength = characterLength.getTargetLength()
        charCountDivisionPerGroup = characterLength.getCharCountDivisionPerGroup(groups, targetLength)
        charsFromTheGroups = characterGroup.getCharsPerGroup(groups, charCountDivisionPerGroup)
        remainingCharsCount = characterLength.getRemainingCharsCount(targetLength, charsFromTheGroups)
        remainingChars = characterGroup.getCharsFromRandomGroups(groups,
                                                                charCountDivisionPerGroup,
                                                                remainingCharsCount)
        result = characterGroup.shuffleIntoString(charsFromTheGroups, remainingChars)
        context["generatedPassword"] = result

    return render(request, template, context)
