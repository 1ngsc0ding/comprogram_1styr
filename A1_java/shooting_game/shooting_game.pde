int score = 0;
String gameState = "PLAY";

// CANNON
float cannonX = 90;
float cannonY = 520;

// SCOPE
float scopeX = 500;
float scopeY = 250;

// POWER
float power = 0;
float maxPower = 100;
boolean charging = false;

// BULLET
float bulletX = 0;
float bulletY = 0;
float vx = 0;
float vy = 0;
boolean bulletActive = false;
float gravity = 0.25;

// TARGET
int targetCount = 5;

float[] targetX = new float[targetCount];
float[] targetY = new float[targetCount];
boolean[] targetAlive = new boolean[targetCount];

float[] targetVX = new float[targetCount];
float[] targetVY = new float[targetCount];

float targetRadius = 28;
float targetSpeedMin = 1.2;
float targetSpeedMax = 2.5;

// HIT EFFECT
float hitX = 0;
float hitY = 0;
int hitTimer = 0;

void setup() {
  size(1100, 650);
  smooth();
  textFont(createFont("Arial", 20));

  spawnAllTargets();
}

void draw() {
  drawBackground();

  if (gameState.equals("PLAY")) {
    updateGame();
  }

  drawCannon();
  drawTargets();
  drawScope();
  drawHUD();

  if (hitTimer > 0) {
    drawHitEffect();
  }
}

void updateGame() {
  scopeX = constrain(mouseX, 150, width - 30);
  scopeY = constrain(mouseY, 70, 450);

  moveTargets();
  updatePower();

  if (bulletActive) {
    moveBullet();
    checkCollision();
  }
}

void drawBackground() {
  background(105, 185, 225);

  drawCloud(170, 100);
  drawCloud(790, 120);

  // Mountains
  noStroke();
  fill(85, 135, 165);

  triangle(0, 470, 190, 270, 370, 470);
  triangle(200, 470, 460, 220, 720, 470);
  triangle(550, 470, 775, 280, 1080, 470);

  // Ground
  fill(80, 150, 55);
  rect(0, 470, width, 35);

  fill(65, 115, 45);
  rect(0, 505, width, 145);
}

void drawCloud(float x, float y) {
  noStroke();
  fill(245, 250, 255, 210);

  ellipse(x, y, 100, 45);
  ellipse(x + 45, y - 10, 100, 55);
  ellipse(x + 90, y + 5, 110, 45);
}


// ============================================
// CANNON
// ============================================

void drawCannon() {
  float angle = atan2(
    scopeY - cannonY,
    scopeX - cannonX
  );

  pushMatrix();

  translate(cannonX, cannonY);
  rotate(angle);

  // Cannon barrel
  stroke(30);
  strokeWeight(4);
  fill(55, 60, 65);

  rect(0, -15, 90, 30, 8);

  // Barrel opening
  fill(25);
  ellipse(88, 0, 28, 36);

  popMatrix();

  // Cannon wheel
  stroke(30);
  strokeWeight(5);
  fill(130, 80, 40);

  ellipse(cannonX, cannonY + 22, 65, 65);

  // Wheel center
  fill(70, 45, 25);
  ellipse(cannonX, cannonY + 22, 20, 20);

  // Cannon base
  noStroke();
  fill(65, 65, 65);

  rect(
    cannonX - 45,
    cannonY + 35,
    90,
    22,
    5
  );
}

void drawScope() {
  stroke(255);
  strokeWeight(3);
  noFill();

  // Scope circle
  ellipse(scopeX, scopeY, 55, 55);

  // Horizontal line
  line(
    scopeX - 38,
    scopeY,
    scopeX + 38,
    scopeY
  );

  // Vertical line
  line(
    scopeX,
    scopeY - 38,
    scopeX,
    scopeY + 38
  );

  // Center
  fill(255);
  ellipse(scopeX, scopeY, 7, 7);

  drawTrajectory();
}

void drawTrajectory() {
  if (bulletActive) {
    return;
  }

  float angle = atan2(
    scopeY - cannonY,
    scopeX - cannonX
  );

  float speed = map(
    power,
    0,
    maxPower,
    5,
    16
  );

  float guideVX = speed * cos(angle);
  float guideVY = speed * sin(angle);

  float px = cannonX;
  float py = cannonY;

  stroke(255, 255, 255, 180);
  strokeWeight(2);

  for (int i = 0; i < 35; i++) {
    px += guideVX * 2;
    py += guideVY * 2;

    guideVY += gravity * 2;

    if (py > height) {
      break;
    }

    ellipse(px, py, 5, 5);
  }
}

void spawnAllTargets() {
  for (int i = 0; i < targetCount; i++) {
    targetAlive[i] = false;
  }

  for (int i = 0; i < targetCount; i++) {
    spawnTarget(i);
  }
}

void spawnTarget(int index) {
  float x;
  float y;
  boolean valid = false;
  int attempts = 0;

  while (!valid && attempts < 1000) {
    x = random(400, width - 60);
    y = random(120, 420);

    valid = true;

    for (int j = 0; j < targetCount; j++) {
      if (j != index && targetAlive[j]) {
        float d = dist(
          x,
          y,
          targetX[j],
          targetY[j]
        );

        if (d < 100) {
          valid = false;
          break;
        }
      }
    }

    if (valid) {
      targetX[index] = x;
      targetY[index] = y;
    }

    attempts++;
  }

  // Fallback position if a free location
  // cannot be found after many attempts.
  if (!valid) {
    targetX[index] = random(400, width - 60);
    targetY[index] = random(120, 420);
  }

  // Random movement direction
  float direction = random(TWO_PI);

  float speed = random(
    targetSpeedMin,
    targetSpeedMax
  );

  targetVX[index] = cos(direction) * speed;
  targetVY[index] = sin(direction) * speed;

  targetAlive[index] = true;
}

void moveTargets() {
  for (int i = 0; i < targetCount; i++) {
    if (targetAlive[i]) {

      // Move
      targetX[i] += targetVX[i];
      targetY[i] += targetVY[i];

      // Left / Right
      if (targetX[i] < 400) {
        targetX[i] = 400;
        targetVX[i] *= -1;
      } else if (targetX[i] > width - 50) {
        targetX[i] = width - 50;
        targetVX[i] *= -1;
      }

      // Top / Bottom
      if (targetY[i] < 100) {
        targetY[i] = 100;
        targetVY[i] *= -1;
      } else if (targetY[i] > 420) {
        targetY[i] = 420;
        targetVY[i] *= -1;
      }
    }
  }
}

void drawTargets() {
  for (int i = 0; i < targetCount; i++) {
    if (targetAlive[i]) {
      drawTarget(targetX[i], targetY[i]);
    }
  }
}

void drawTarget(float x, float y) {
  // Stand
  stroke(70);
  strokeWeight(5);

  line(x, y + 25, x, y + 75);
  line(x, y + 55, x - 18, y + 75);
  line(x, y + 55, x + 18, y + 75);

  // Outer white circle
  noStroke();
  fill(245);
  ellipse(x, y, 65, 65);

  // Red circle
  fill(220, 50, 40);
  ellipse(x, y, 52, 52);

  // White circle
  fill(250);
  ellipse(x, y, 36, 36);

  // Center
  fill(220, 50, 40);
  ellipse(x, y, 20, 20);
}

void updatePower() {
  if (mousePressed && !bulletActive) {
    charging = true;

    power += 1.5;

    if (power >= maxPower) {
      power = maxPower;
    }

  } else if (charging && !mousePressed) {
    charging = false;
    shoot();
  }
}

void shoot() {
  if (power <= 0) {
    return;
  }

  // Calculate shooting angle
  float angle = atan2(
    scopeY - cannonY,
    scopeX - cannonX
  );

  // Convert power to speed
  float speed = map(
    power,
    0,
    maxPower,
    5,
    18
  );

  // Projectile motion
  vx = speed * cos(angle);
  vy = speed * sin(angle);

  // Starting position
  bulletX = cannonX;
  bulletY = cannonY;

  bulletActive = true;

  // Reset power
  power = 0;
}

void moveBullet() {
  // X movement
  bulletX += vx;

  // Y movement
  bulletY += vy;

  // Gravity
  vy += gravity;

  // Outside screen
  if (
    bulletX < 0 ||
    bulletX > width ||
    bulletY < 0 ||
    bulletY > height
  ) {
    bulletActive = false;
  }
}

void drawBullet() {
  if (!bulletActive) {
    return;
  }

  noStroke();

  // Bullet
  fill(40);
  ellipse(bulletX, bulletY, 14, 14);

  // Bullet trail
  fill(80, 80, 80, 100);

  ellipse(
    bulletX - vx * 2,
    bulletY - vy * 2,
    8,
    8
  );
}

void checkCollision() {
  for (int i = 0; i < targetCount; i++) {
    if (targetAlive[i]) {

      float d = dist(
        bulletX,
        bulletY,
        targetX[i],
        targetY[i]
      );

      if (d < targetRadius) {

        // Hit target
        targetAlive[i] = false;

        // Add score
        score += 100;

        // Hit effect position
        hitX = targetX[i];
        hitY = targetY[i];

        hitTimer = 20;

        // Stop bullet
        bulletActive = false;

        // Spawn new target
        spawnTarget(i);

        // Only hit one target per bullet
        break;
      }
    }
  }
}

void drawHitEffect() {
  stroke(255, 220, 50);
  strokeWeight(5);
  noFill();

  float effectSize = (20 - hitTimer) * 5;

  ellipse(
    hitX,
    hitY,
    effectSize,
    effectSize
  );

  hitTimer--;
}

void drawHUD() {
  // SCORE
  fill(255);

  textAlign(LEFT, TOP);
  textSize(28);

  text(
    "SCORE: " + score,
    25,
    20
  );

  // POWER TITLE
  textAlign(CENTER, CENTER);
  textSize(20);
  fill(255);

  text("POWER", 775, 20);

  // POWER BACKGROUND
  fill(30, 40, 45);
  stroke(255);
  strokeWeight(3);

  rect(650, 35, 250, 28, 10);

  // POWER BAR
  noStroke();
  fill(255, 190, 30);

  float powerWidth = map(
    power,
    0,
    maxPower,
    0,
    250
  );

  rect(650, 35, powerWidth, 28, 10);

  fill(20, 30, 40, 210);

  rect(680, 80, 280, 90, 10);

  fill(255);
  textSize(17);

  text("MOVE MOUSE TO AIM", 820, 105);

  fill(255, 210, 40);
  text("HOLD MOUSE = POWER", 820, 130);

  fill(255);
  text("RELEASE = SHOOT", 820, 155);

  fill(20, 30, 40, 220);

  rect(20, 580, 210, 45, 8);

  fill(255);
  textSize(16);

  text("R = RESTART", 125, 602);

  drawBullet();
}


void keyPressed() {
  if (key == 'r' || key == 'R') {

    score = 0;
    power = 0;

    bulletActive = false;
    charging = false;

    hitTimer = 0;

    spawnAllTargets();
  }
}
