# ============================================
# PROJECTILE SHOOTING GAME
# Processing Python Mode
# ============================================


# ============================================
# GAME
# ============================================

score = 0
gameState = "PLAY"


# ============================================
# CANNON
# ============================================

cannonX = 90
cannonY = 520


# ============================================
# SCOPE
# ============================================

scopeX = 500
scopeY = 250


# ============================================
# POWER
# ============================================

power = 0
maxPower = 100
charging = False


# ============================================
# BULLET
# ============================================

bulletX = 0
bulletY = 0

vx = 0
vy = 0

bulletActive = False

gravity = 0.25


# ============================================
# TARGET
# ============================================

targetCount = 5

targetX = []
targetY = []
targetAlive = []

targetVX = []
targetVY = []

targetRadius = 28

targetSpeedMin = 1.2
targetSpeedMax = 2.5


# ============================================
# HIT EFFECT
# ============================================

hitX = 0
hitY = 0
hitTimer = 0


# ============================================
# SETUP
# ============================================

def setup():

    size(1100, 650)

    smooth()

    textFont(
        createFont("Arial", 20)
    )

    spawnAllTargets()


# ============================================
# MAIN LOOP
# ============================================

def draw():

    drawBackground()

    if gameState == "PLAY":

        updateGame()

    drawCannon()
    drawTargets()
    drawScope()
    drawHUD()

    if hitTimer > 0:

        drawHitEffect()


# ============================================
# UPDATE GAME
# ============================================

def updateGame():

    global scopeX
    global scopeY

    # Scope follows mouse
    scopeX = constrain(
        mouseX,
        150,
        width - 30
    )

    scopeY = constrain(
        mouseY,
        70,
        450
    )

    # Move targets
    moveTargets()

    # Update power
    updatePower()

    # Move bullet
    if bulletActive:

        moveBullet()

        checkCollision()


# ============================================
# BACKGROUND
# ============================================

def drawBackground():

    # Sky
    background(
        105,
        185,
        225
    )

    # Clouds
    drawCloud(
        170,
        100
    )

    drawCloud(
        790,
        120
    )

    # Mountains
    noStroke()

    fill(
        85,
        135,
        165
    )

    triangle(
        0,
        470,
        190,
        270,
        370,
        470
    )

    triangle(
        200,
        470,
        460,
        220,
        720,
        470
    )

    triangle(
        550,
        470,
        775,
        280,
        1080,
        470
    )

    # Ground
    fill(
        80,
        150,
        55
    )

    rect(
        0,
        470,
        width,
        35
    )

    fill(
        65,
        115,
        45
    )

    rect(
        0,
        505,
        width,
        145
    )


# ============================================
# CLOUD
# ============================================

def drawCloud(x, y):

    noStroke()

    fill(
        245,
        250,
        255,
        210
    )

    ellipse(
        x,
        y,
        100,
        45
    )

    ellipse(
        x + 45,
        y - 10,
        100,
        55
    )

    ellipse(
        x + 90,
        y + 5,
        110,
        45
    )


# ============================================
# CANNON
# ============================================

def drawCannon():

    # Calculate angle
    angle = atan2(
        scopeY - cannonY,
        scopeX - cannonX
    )

    pushMatrix()

    translate(
        cannonX,
        cannonY
    )

    rotate(angle)

    # Cannon barrel
    stroke(30)

    strokeWeight(4)

    fill(
        55,
        60,
        65
    )

    rect(
        0,
        -15,
        90,
        30,
        8
    )

    # Barrel opening
    fill(25)

    ellipse(
        88,
        0,
        28,
        36
    )

    popMatrix()

    # Cannon wheel
    stroke(30)

    strokeWeight(5)

    fill(
        130,
        80,
        40
    )

    ellipse(
        cannonX,
        cannonY + 22,
        65,
        65
    )

    # Wheel center
    fill(
        70,
        45,
        25
    )

    ellipse(
        cannonX,
        cannonY + 22,
        20,
        20
    )

    # Cannon base
    noStroke()

    fill(
        65,
        65,
        65
    )

    rect(
        cannonX - 45,
        cannonY + 35,
        90,
        22,
        5
    )


# ============================================
# SCOPE
# ============================================

def drawScope():

    stroke(255)

    strokeWeight(3)

    noFill()

    # Scope circle
    ellipse(
        scopeX,
        scopeY,
        55,
        55
    )

    # Horizontal line
    line(
        scopeX - 38,
        scopeY,
        scopeX + 38,
        scopeY
    )

    # Vertical line
    line(
        scopeX,
        scopeY - 38,
        scopeX,
        scopeY + 38
    )

    # Center
    fill(255)

    ellipse(
        scopeX,
        scopeY,
        7,
        7
    )

    # Aim trajectory
    drawTrajectory()


# ============================================
# TRAJECTORY
# ============================================

def drawTrajectory():

    if bulletActive:

        return

    angle = atan2(
        scopeY - cannonY,
        scopeX - cannonX
    )

    speed = map(
        power,
        0,
        maxPower,
        5,
        16
    )

    guideVX = speed * cos(angle)
    guideVY = speed * sin(angle)

    px = cannonX
    py = cannonY

    stroke(
        255,
        255,
        255,
        180
    )

    strokeWeight(2)

    for i in range(35):

        px += guideVX * 2
        py += guideVY * 2

        guideVY += gravity * 2

        if py > height:

            break

        ellipse(
            px,
            py,
            5,
            5
        )


# ============================================
# SPAWN ALL TARGETS
# ============================================

def spawnAllTargets():

    targetX[:] = []
    targetY[:] = []
    targetAlive[:] = []

    targetVX[:] = []
    targetVY[:] = []

    i = 0

    while i < targetCount:

        spawnTarget(i)

        i += 1


# ============================================
# SPAWN TARGET
# ============================================

def spawnTarget(index):

    valid = False

    while not valid:

        x = random(
            400,
            width - 60
        )

        y = random(
            120,
            420
        )

        valid = True

        j = 0

        while j < len(targetX):

            # Don't compare target with itself
            if j != index:

                d = dist(
                    x,
                    y,
                    targetX[j],
                    targetY[j]
                )

                if d < 100:

                    valid = False

            j += 1

    # Random movement direction
    direction = random(
        TWO_PI
    )

    speed = random(
        targetSpeedMin,
        targetSpeedMax
    )

    newVX = cos(direction) * speed
    newVY = sin(direction) * speed

    if index < len(targetX):

        targetX[index] = x
        targetY[index] = y
        targetAlive[index] = True

        targetVX[index] = newVX
        targetVY[index] = newVY

    else:

        targetX.append(x)
        targetY.append(y)
        targetAlive.append(True)

        targetVX.append(newVX)
        targetVY.append(newVY)


# ============================================
# MOVE TARGETS
# ============================================

def moveTargets():

    i = 0

    while i < len(targetX):

        if targetAlive[i]:

            # Move
            targetX[i] += targetVX[i]
            targetY[i] += targetVY[i]

            # Left / Right
            if targetX[i] < 400:

                targetX[i] = 400

                targetVX[i] *= -1

            elif targetX[i] > width - 50:

                targetX[i] = width - 50

                targetVX[i] *= -1

            # Top / Bottom
            if targetY[i] < 100:

                targetY[i] = 100

                targetVY[i] *= -1

            elif targetY[i] > 420:

                targetY[i] = 420

                targetVY[i] *= -1

        i += 1


# ============================================
# DRAW TARGETS
# ============================================

def drawTargets():

    i = 0

    while i < len(targetX):

        if targetAlive[i]:

            drawTarget(
                targetX[i],
                targetY[i]
            )

        i += 1


# ============================================
# DRAW TARGET
# ============================================

def drawTarget(x, y):

    # Stand
    stroke(70)

    strokeWeight(5)

    line(
        x,
        y + 25,
        x,
        y + 75
    )

    line(
        x,
        y + 55,
        x - 18,
        y + 75
    )

    line(
        x,
        y + 55,
        x + 18,
        y + 75
    )

    # Outer white circle
    noStroke()

    fill(245)

    ellipse(
        x,
        y,
        65,
        65
    )

    # Red circle
    fill(
        220,
        50,
        40
    )

    ellipse(
        x,
        y,
        52,
        52
    )

    # White circle
    fill(250)

    ellipse(
        x,
        y,
        36,
        36
    )

    # Center
    fill(
        220,
        50,
        40
    )

    ellipse(
        x,
        y,
        20,
        20
    )


# ============================================
# POWER
# ============================================

def updatePower():

    global power
    global charging

    if mousePressed and not bulletActive:

        charging = True

        power += 1.5

        if power >= maxPower:

            power = maxPower

    elif charging and not mousePressed:

        charging = False

        shoot()


# ============================================
# SHOOT
# ============================================

def shoot():

    global bulletX
    global bulletY
    global vx
    global vy
    global bulletActive
    global power

    if power <= 0:

        return

    # Calculate shooting angle
    angle = atan2(
        scopeY - cannonY,
        scopeX - cannonX
    )

    # Convert Power to Speed
    speed = map(
        power,
        0,
        maxPower,
        5,
        18
    )

    # Projectile Motion
    vx = speed * cos(angle)
    vy = speed * sin(angle)

    # Starting position
    bulletX = cannonX
    bulletY = cannonY

    bulletActive = True

    # Reset power
    power = 0


# ============================================
# MOVE BULLET
# ============================================

def moveBullet():

    global bulletX
    global bulletY
    global vy
    global bulletActive

    # X movement
    bulletX += vx

    # Y movement
    bulletY += vy

    # Gravity
    vy += gravity

    # Outside screen
    if (
        bulletX < 0 or
        bulletX > width or
        bulletY < 0 or
        bulletY > height
    ):

        bulletActive = False


# ============================================
# DRAW BULLET
# ============================================

def drawBullet():

    if not bulletActive:

        return

    noStroke()

    # Bullet
    fill(40)

    ellipse(
        bulletX,
        bulletY,
        14,
        14
    )

    # Bullet trail
    fill(
        80,
        80,
        80,
        100
    )

    ellipse(
        bulletX - vx * 2,
        bulletY - vy * 2,
        8,
        8
    )


# ============================================
# COLLISION
# ============================================

def checkCollision():

    global score
    global bulletActive
    global hitX
    global hitY
    global hitTimer

    i = 0

    while i < len(targetX):

        if targetAlive[i]:

            d = dist(
                bulletX,
                bulletY,
                targetX[i],
                targetY[i]
            )

            if d < targetRadius:

                # Hit target
                targetAlive[i] = False

                # Add score
                score += 100

                # Hit effect position
                hitX = targetX[i]
                hitY = targetY[i]

                hitTimer = 20

                # Stop bullet
                bulletActive = False

                # Spawn new target
                spawnTarget(i)

        i += 1


# ============================================
# HIT EFFECT
# ============================================

def drawHitEffect():

    global hitTimer

    stroke(
        255,
        220,
        50
    )

    strokeWeight(5)

    noFill()

    effectSize = (
        20 - hitTimer
    ) * 5

    ellipse(
        hitX,
        hitY,
        effectSize,
        effectSize
    )

    hitTimer -= 1


# ============================================
# HUD
# ============================================

def drawHUD():

    # ========================
    # SCORE
    # ========================

    fill(255)

    textAlign(
        LEFT,
        TOP
    )

    textSize(28)

    text(
        "SCORE: " + str(score),
        25,
        20
    )

    # ========================
    # POWER TITLE
    # ========================

    textAlign(
        CENTER,
        CENTER
    )

    textSize(20)

    fill(255)

    text(
        "POWER",
        775,
        20
    )

    # ========================
    # POWER BACKGROUND
    # ========================

    fill(
        30,
        40,
        45
    )

    stroke(255)

    strokeWeight(3)

    rect(
        650,
        35,
        250,
        28,
        10
    )

    # ========================
    # POWER BAR
    # ========================

    noStroke()

    fill(
        255,
        190,
        30
    )

    powerWidth = map(
        power,
        0,
        maxPower,
        0,
        250
    )

    rect(
        650,
        35,
        powerWidth,
        28,
        10
    )

    # ========================
    # INSTRUCTIONS
    # ========================

    fill(
        20,
        30,
        40,
        210
    )

    rect(
        680,
        80,
        280,
        90,
        10
    )

    fill(255)

    textSize(17)

    text(
        "MOVE MOUSE TO AIM",
        820,
        105
    )

    fill(
        255,
        210,
        40
    )

    text(
        "HOLD MOUSE = POWER",
        820,
        130
    )

    fill(255)

    text(
        "RELEASE = SHOOT",
        820,
        155
    )

    # ========================
    # RESTART BUTTON
    # ========================

    fill(
        20,
        30,
        40,
        220
    )

    rect(
        20,
        580,
        210,
        45,
        8
    )

    fill(255)

    textSize(16)

    text(
        "R = RESTART",
        125,
        602
    )

    # ========================
    # BULLET
    # ========================

    drawBullet()


# ============================================
# KEYBOARD
# ============================================

def keyPressed():

    global score
    global power
    global bulletActive
    global charging

    if key == 'r' or key == 'R':

        score = 0

        power = 0

        bulletActive = False

        charging = False

        spawnAllTargets()
