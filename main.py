# This code is vastly inefficient, especially the middle sections.
# Unfortunately, my meager knowledge is not sufficient to optimise this, so ¯\_(ツ)_/¯
import math
import os
import sympy

os.system('clear')

file = open('trigResults.txt', mode = 'a')

isRight = False
triangleInput = str(input('Is the triangle right-angled? '))

if triangleInput.lower() == 'y' or triangleInput.lower() == 'yes':
  isRight = True
elif triangleInput.lower() == 'n' or triangleInput.lower() == 'no':
  pass
else:
  print('Invalid Input.')
  exit()

optionInput = str(input('Are you looking for an angle or length? '))
angle = False
length = False

if optionInput.lower() == 'a' or optionInput.lower() == 'angle':
  angle = True
elif optionInput.lower() == 'l' or optionInput.lower() == 'length':
  length = True
else:
  print('Invalid Input.')
  exit()

# -- Right Angled Triangles -- #

while angle and isRight:
  sideInput1 = str(input('Which sides are you given [1]? (Adj/Opp/Hyp) '))
  sideInput2 = str(input('Which sides are you given [2]? (Adj/Opp/Hyp) '))

  lengthInput1 = float(input('Side 1 length? '))
  lengthInput2 = float(input('Side 2 length? '))

  # -- TOA -- #
  if sideInput1 == 'opp' and sideInput2 == 'adj':
    output = round(math.degrees(math.atan(math.radians(lengthInput1) / math.radians(lengthInput2))), 2)
    print(f'\nLet Θ be the unknown angle.\ntanΘ = Opposite / Adjacent\ntanΘ = {lengthInput1} / {lengthInput2}')
    print(f'\nΘ = arctan({lengthInput1} / {lengthInput2})\nΘ = {output}° (2 D.P)')

    file.write(f'\nLet Θ be the unknown angle.\ntanΘ = Opposite / Adjacent\ntanΘ = {lengthInput1} / {lengthInput2}')
    file.write(f'\nΘ = arctan({lengthInput1} / {lengthInput2})\nΘ = {output}° (2 D.P)')
    exit()

  elif sideInput1 == 'adj' and sideInput2 == 'opp':
    output = round(math.degrees(math.atan(math.radians(lengthInput2) / math.radians(lengthInput1))), 2)
    print(f'\nLet Θ be the unknown angle.\ntanΘ = Opposite / Adjacent\ntanΘ = {lengthInput2} / {lengthInput1}')
    print(f'Θ = arctan({lengthInput2} / {lengthInput1})\nΘ = {output}°')

    file.write('\nLet Θ be the unknown angle.\ntanΘ = Opposite / Adjacent\ntanΘ = {lengthInput2} / {lengthInput1}')
    file.write(f'Θ = arctan({lengthInput2} / {lengthInput1})\nΘ = {output}°')
    exit()

  # -- CAH -- #
  elif sideInput1 == 'adj' and sideInput2 == 'hyp':
    try:
      output = round(math.degrees(math.acos(math.radians(lengthInput1) / math.radians(lengthInput2))), 2)
      print(f'\nLet Θ be the unknown angle.\ncosΘ = Adjacent / Hypotenuse\ncosΘ = {lengthInput1} / {lengthInput2}')
      print(f'\nΘ = arccos({lengthInput1} / {lengthInput2})\nΘ = {output}°')

      file.write(f'\nLet Θ be the unknown angle.\ncosΘ = Adjacent / Hypotenuse\ncosΘ = {lengthInput1} / {lengthInput2}')
      file.write(f'\nΘ = arccos({lengthInput1} / {lengthInput2})\nΘ = {output}°')
      exit()

    except ValueError:
      print('\nNot a real value. Check if the adjacent side was longer than the hypotenuse.')
      print(f'Values provided:\nAdj: {lengthInput1}\nHyp: {lengthInput2}')
      exit()

  elif sideInput1 == 'hyp' and sideInput2 == 'adj':
    try:
      output = round(math.degrees(math.acos(math.radians(lengthInput2) / math.radians(lengthInput1))), 2)
      print(f'\nLet Θ be the unknown angle.\ncosΘ = Adjacent / Hypotenuse\ncosΘ = {lengthInput2} / {lengthInput1}')
      print(f'Θ = arccos({lengthInput2} / {lengthInput1})\nΘ = {output}°')

      file.write(f'\nLet Θ be the unknown angle.\ncosΘ = Adjacent / Hypotenuse\ncosΘ = {lengthInput2} / {lengthInput1}')
      file.write(f'Θ = arccos({lengthInput2} / {lengthInput1})\nΘ = {output}°')
      exit()

    except ValueError:
      print('\nNot a real value. Check if the adjacent side was longer than the hypotenuse.')
      print(f'Values provided:\nAdj: {sideInput2}\nHyp: {lengthInput2}')
      exit()

  # -- SOH -- #
  elif sideInput1 == 'opp' and sideInput2 == 'hyp':
    try:
      output = round(math.degrees(math.asin(math.radians(lengthInput1) / math.radians(lengthInput2))), 2)
      print(f'\nLet Θ be the unknown angle.\nsinΘ = Opposite / Hypotenuse\ncosΘ = {lengthInput1} / {lengthInput2}')
      print(f'Θ = arccos({lengthInput1} / {lengthInput2})\nΘ = {output}°')

      file.write(f'\nLet Θ be the unknown angle.\nsinΘ = Opposite / Hypotenuse\ncosΘ = {lengthInput1} / {lengthInput2}')
      file.write(f'Θ = arccos({lengthInput1} / {lengthInput2})\nΘ = {output}°')
      exit()

    except ValueError:
      print('\nNot a real value. Check if the adjacent side was longer than the hypotenuse.')
      print(f'Values provided:\nOpp: {lengthInput1}\nHyp: {lengthInput2}')
      exit()

  elif sideInput1 == 'hyp' and sideInput2 == 'opp':
    try:
      output = round(math.degrees(math.asin(math.radians(lengthInput2) / math.radians(lengthInput1))), 2)
      print(f'\nLet Θ be the unknown angle.\nsinΘ = Opposite / Hypotenuse\ncosΘ = {lengthInput2} / {lengthInput1}')
      print(f'Θ = arccos({lengthInput2} / {lengthInput1})\nΘ = {output}°')

      file.write(f'\nLet Θ be the unknown angle.\nsinΘ = Opposite / Hypotenuse\ncosΘ = {lengthInput2} / {lengthInput1}')
      file.write(f'Θ = arccos({lengthInput2} / {lengthInput1})\nΘ = {output}°')
      exit()

    except ValueError:
      print('\nNot a real value. Check if the adjacent side was longer than the hypotenuse.')
      print(f'Values provided:\nOpp: {lengthInput2}\nHyp: {lengthInput1}')
      exit()

  else:
    print('\nInvalid Input.')
    exit()

while length and isRight:
  obj = input('Which side are you looking for? (Adj/Opp/Hyp) ')
  possibleSide1 = ''
  possibleSide2 = ''

  if obj == 'adj':
    possibleSide1 = 'Opp'
    possibleSide2 = 'Hyp'
  elif obj == 'opp':
    possibleSide1 = 'Adj'
    possibleSide2 = 'Hyp'
  elif obj == 'hyp':
    possibleSide1 = 'Opp'
    possibleSide2 = 'Adj'

  sideGiven = input(f'What other side are you given? ({possibleSide1}/{possibleSide2}) ')
  givenLength = float(input('Length of side? '))
  givenAngle = float(input('Angle given? '))

  # -- Adjacent -- #
  if obj == 'adj' and sideGiven == 'opp':
    output = round(givenLength / math.tan(math.radians(givenAngle)), 2)
    print(f'\nAdjacent = Opposite / tan(Θ)\nAdjacent = {givenLength} / tan({givenAngle})')
    print(f'Adjacent Length = {output}')

    file.write(f'\nAdjacent = Opposite / tan(Θ)\nAdjacent = {givenLength} / tan({givenAngle})')
    file.write(f'Adjacent Length = {output}')

    exit()

  elif obj == 'adj' and sideGiven == 'hyp':
    try:
      output = round(givenLength * math.cos(math.radians(givenAngle)), 2)
      print(f'\ncos(Θ) = Adjacent / Hypotenuse\nAdjacent = {givenLength} * cos({givenAngle})')
      print(f'Adjacent Length = {output}')

      file.write(f'\ncos(Θ) = Adjacent / Hypotenuse\nAdjacent = {givenLength} * cos({givenAngle})')
      file.write(f'Adjacent Length = {output}')

    except ValueError:
      print('Something went wrong. Check your values and retry.')

  # -- Hypotenuse -- #
  elif obj == 'hyp' and sideGiven == 'adj':
    try:
      output = round(givenLength / math.cos(math.radians(givenAngle)), 2)
      print(f'\ncos(Θ) = Adjacent / Hypotenuse\nHypotenuse = {givenLength} / cos({givenAngle})')
      print(f'Hypotenuse Length = {output}')

      file.write(f'\ncos(Θ) = Adjacent / Hypotenuse\nHypotenuse = {givenLength} / cos({givenAngle})')
      file.write(f'Hypotenuse Length = {output}')

    except ValueError:
      print('Something went wrong. Check your values and retry.')

  elif obj == 'hyp' and sideGiven == 'opp':
    try:
      output = round(givenLength / math.sin(math.radians(givenAngle)), 2)
      print(f'\nsin(Θ) = Opposite / Hypotenuse\nHypotenuse = {givenLength} / cos({givenAngle})')
      print(f'Hypotenuse Length = {output}')

      file.write(f'\nsin(Θ) = Opposite / Hypotenuse\nHypotenuse = {givenLength} / cos({givenAngle})')
      file.write(f'Hypotenuse Length = {output}')

    except ValueError:
      print('Something went wrong. Check your values and retry.')

  # -- Opposite -- #
  elif obj == 'opp' and sideGiven == 'hyp':
    try:
      output = round(givenLength * math.sin(math.radians(givenAngle)), 2)
      print(f'\nsin(Θ) = Opposite / Hypotenuse\nOpposite = {givenLength} * sin({givenAngle})')
      print(f'Opposite Length = {output}')

      file.write(f'\nsin(Θ) = Opposite / Hypotenuse\nOpposite = {givenLength} * sin({givenAngle})')
      file.write(f'Opposite Length = {output}')

    except ValueError:
      print('Something went wrong. Check your values and retry.')

  elif obj == 'opp' and sideGiven == 'adj':
    try:
      output = round(givenLength * math.tan(math.radians(givenAngle)), 2)
      print(f'\ntan(Θ) = Opposite / Adjacent\nOpposite = {givenLength} * tan({givenAngle})')
      print(f'Opposite Length = {output}')

      file.write(f'\ntan(Θ) = Opposite / Adjacent\nOpposite = {givenLength} * tan({givenAngle})')
      file.write(f'Opposite Length = {output}')

    except ValueError:
      print('Something went wrong. Check your values and retry.')

  # -- Exceptions -- #
  elif obj == sideGiven:
    print('Invalid inputs.')
    exit()


# -- Non-Right Angled Triangles -- #
while not isRight:
  useSineRule = False
  useCosineRule = False

  sidesInfo = input('Are you given all sides? ')
  furtherInfo = ''

  if sidesInfo.lower() == 'no' or sidesInfo.lower() == 'n':
    furtherInfo = input('Do you have 2 sides and the angle between them? ')
  elif sidesInfo.lower() == 'yes' or sidesInfo.lower() == 'y':
    useCosineRule = True # Used to fine ANGLE (3 sides)

  if furtherInfo.lower() == 'no' or furtherInfo.lower() == 'n':
    useSineRule = True # Used to find ANGLE (2 sides WITHOUT corresponding angle)
  elif furtherInfo.lower() == 'yes' or furtherInfo.lower() == 'y':
    useCosineRule = True # Used to find LENGTH (2 sides with CORRESPONDING angle)

  while not isRight and angle and useCosineRule:
    if sidesInfo == 'y' or sidesInfo == 'yes':
      side1Length = float(input('Side α length? This is the side opposite angle A: ' ))
      side2Length = float(input('Side β length? This is the side opposite angle B: '))
      side3Length = float(input('Side γ length? This is the side opposite the angle you want: '))

      leftSum = side3Length ** 2
      rightSum1 = (side1Length ** 2) + (side2Length ** 2)
      rightSum2 = (2 * side1Length * side2Length) * -1

      finalLeftSum = leftSum - rightSum1
      finalSum = round(finalLeftSum / rightSum2, 2)

      output = round(math.degrees(math.acos(finalLeftSum / rightSum2)), 2)
      print(f'\nγ² = α² + β² - 2αβ * cos(C)\n{side3Length}² = {side1Length}² + {side2Length}² - 2 * {side1Length} * {side2Length} * cos(γ)')
      print(f'{leftSum} = {rightSum1} + ({rightSum2}) * cos(γ)\n{finalLeftSum} = ({rightSum2}) * cos(γ)')
      print(f'γ = arccos({finalLeftSum} / {rightSum2})\nγ = {output}° (2 D.P)')

      file.write(f'\nγ² = α² + β² - 2αβ * cos(C)\n{side3Length}² = {side1Length}² + {side2Length}² - 2 * {side1Length} * {side2Length} * cos(γ)')
      file.write(f'{leftSum} = {rightSum1} + ({rightSum2}) * cos(γ)\n{finalLeftSum} = ({rightSum2}) * cos(γ)')
      file.write(f'γ = arccos({finalLeftSum} / {rightSum2})\nγ = {output}° (2 D.P)')
      exit()

  while length and useCosineRule and (sidesInfo.lower() == 'yes' or sidesInfo.lower() == 'y'):
    print('Are you fucking stupid or something? ')
    exit()

  while useSineRule and (furtherInfo.lower() == 'no' or furtherInfo.lower() == 'n') and angle:
    angle = float(input('Angle size? '))
    correspondingSide = float(input('Length of side corresponding to given angle? '))
    otherSide = float(input('Length of other side? '))

    try:
      sineAngle = math.sin(math.radians(angle))
      output = round(math.degrees(math.asin((sineAngle / correspondingSide) * otherSide)), 2)
      print(f'\nLet Θ be the unknown angle\nsin(A) / α = sin(B) / β ...\nsin({angle}) / {correspondingSide} = sin(Θ) / {otherSide}')
      print(f'sin(Θ) = {otherSide} * (sin({angle} / {correspondingSide}))\nΘ = sin^-1({otherSide} * (sin({angle} / {correspondingSide}))')
      print(f'Θ = {output} (2 D.P)')
      exit()

    except ValueError:
      print('\nValues for sides are invalid for calculation. ')
      print(f'Provided values:\nAngle: {angle}\nCorresponding Side: {correspondingSide}\nOther Side: {otherSide}')
      exit()

  while not isRight and length:
    if (furtherInfo.lower() == 'yes' or furtherInfo.lower() == 'y') and useCosineRule:
      try:
        side1Length = float(input('Side length [1]? '))
        side2Length = float(input('Side length [2]? '))
        angle = float(input('Angle? '))

        squaredLen1 = side1Length ** 2
        squaredLen2 = side2Length ** 2

        output = round(sympy.sqrt(squaredLen1 + squaredLen2 - ((2 * side1Length * side2Length) * math.cos(math.radians(angle)))), 2)
        print(f'\nγ² = α² + β² - 2αβ * cos(C)\nγ² = {squaredLen1 + squaredLen2} - {2 * side1Length * side2Length} * cos({angle})')
        print(f'γ = sqrt({output ** 2})\nγ = {output}')
        exit()

      except ValueError:
        print('\nValues are invalid for calculation.')
        exit()

    elif (furtherInfo.lower() == 'no' or furtherInfo.lower() == 'n') and useSineRule:
      reallyFarInfo = input('Do you have 2 angles and 1 side? ')

      if reallyFarInfo.lower() == 'yes' or reallyFarInfo.lower() == 'y':
        try:
          correspondingSide = float(input('Length of side corresponding to one of the given angles? '))
          correspondingAngle = float(input('Angle size (corresponding to given side)? '))
          otherAngle = float(input('Other given angle? '))

          output = (correspondingSide / math.sin(math.radians(correspondingAngle))) * math.sin(math.radians(otherAngle))
          print(f'\nLet x be the unknown length\nx / sin({otherAngle}) = {correspondingSide} / sin({correspondingAngle})')
          print(f'x = ({correspondingSide} / sin({correspondingAngle})) * sin({otherAngle})\nx = {round(output, 2)}')
          exit()

        except ValueError:
          print('\nValues are invalid for calculation.')
          exit()
