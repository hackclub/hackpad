#include <Wire.h>
#include <Adafruit_MCP23008.h>
#include <Encoder.h>
#include <Adafruit_NeoPixel.h>

#define I2C_ADDRESS 0x20  // Adresse I2C du MCP23008
#define NUM_BUTTONS 16     // 4 rangées x 4 colonnes
#define NUM_LEDS 8         // Nombre de LEDs adressables
#define LED_PIN 0          // Pin où sont connectées les LEDs WS2812

// Définir les encodeurs sur les pins P26, P27 et P1, P2
Encoder encoder1(26, 27);
Encoder encoder2(1, 2);

// Instancier les objets pour le MCP23008 et les LEDs
Adafruit_MCP23008 mcp;
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

// Variables pour stocker l'état des boutons et des encodeurs
long encoder1Position = 0;
long encoder2Position = 0;
int lastButtonState[NUM_BUTTONS] = {0};

// Fonction pour lire la matrice de boutons via MCP23008
void readButtonMatrix() {
  // Lire les rangées du MCP23008 (comme si on les "scannait")
  for (int row = 4; row < 8; row++) {
    mcp.pinMode(row, OUTPUT);   // Configurer les pins de rangées en sortie
    mcp.digitalWrite(row, LOW); // Sélectionner une rangée
    
    // Lire chaque colonne
    for (int col = 0; col < 4; col++) {
      mcp.pinMode(col, INPUT);  // Configurer les pins de colonnes en entrée
      int buttonIndex = (row - 4) * 4 + col; // Calculer l'indice du bouton
      int buttonState = !mcp.digitalRead(col); // Lire l'état du bouton (inversé car pull-up)
      
      if (buttonState != lastButtonState[buttonIndex]) {
        if (buttonState) {
          // Bouton pressé
          Serial.print("Bouton appuyé: ");
          Serial.println(buttonIndex);
          // Ici, tu peux ajouter une fonction qui exécute une action spécifique.
        } else {
          // Bouton relâché
          Serial.print("Bouton relâché: ");
          Serial.println(buttonIndex);
        }
        lastButtonState[buttonIndex] = buttonState;
      }
    }
    
    // Désélectionner la rangée avant de passer à la suivante
    mcp.digitalWrite(row, HIGH);
  }
}

// Initialiser le MCP23008, les LEDs et le bus I²C
void setup() {
  Serial.begin(115200);
  
  // Initialisation du MCP23008
  Wire.begin();
  mcp.begin(I2C_ADDRESS);

  // Configurer les LEDs WS2812
  strip.begin();
  strip.show(); // Initialiser toutes les LEDs éteintes

  // Configurer les pins de l'extendeur
  for (int row = 4; row < 8; row++) {
    mcp.pinMode(row, OUTPUT);
    mcp.digitalWrite(row, HIGH); // Désactiver toutes les rangées au départ
  }
  for (int col = 0; col < 4; col++) {
    mcp.pinMode(col, INPUT);
  }
}

// Boucle principale pour lire les boutons et les encodeurs
void loop() {
  // Lire les boutons via MCP23008
  readButtonMatrix();

  // Lire les positions des encodeurs rotatifs
  long newEncoder1Pos = encoder1.read();
  long newEncoder2Pos = encoder2.read();

  if (newEncoder1Pos != encoder1Position) {
    Serial.print("Encoder 1 position: ");
    Serial.println(newEncoder1Pos);
    encoder1Position = newEncoder1Pos;
    // Action liée à l'encodeur 1
  }

  if (newEncoder2Pos != encoder2Position) {
    Serial.print("Encoder 2 position: ");
    Serial.println(newEncoder2Pos);
    encoder2Position = newEncoder2Pos;
    // Action liée à l'encodeur 2
  }

  // Ici, tu peux ajouter du code pour contrôler les LEDs ou exécuter d'autres actions
}
