#include <SoftwareSerial.h> // Incluir la librería para el manejo de Bluetooth

#define ML_Ctrl 2 // Define el pin de control de dirección del motor A
#define ML_PWM 6 // Define el pin de control PWM del motor A
#define MR_Ctrl 4 // Define el pin de control de dirección del motor B
#define MR_PWM 5 // Define el pin de control PWM del motor B

SoftwareSerial bluetooth(0, 1); // Configurar los pines RX y TX del Bluetooth

void setup()
{
  pinMode(ML_Ctrl, OUTPUT); // Pone el pin de control de dirección del motor A en salida
  pinMode(ML_PWM, OUTPUT); // Pone el pin de control PWM del motor A en salida
  pinMode(MR_Ctrl, OUTPUT); // Pone el pin de control de dirección del motor B en salida
  pinMode(MR_PWM, OUTPUT); // Pone el pin de control PWM del motor B en salida

  // Inicializar la comunicación Bluetooth
  bluetooth.begin(9600);
}

void loop()
{
  if (bluetooth.available()) {
    char command = bluetooth.read();

    if (command == 'R') {
      digitalWrite(ML_Ctrl, LOW); // Pone el pin de control de dirección del motor A a LOW
      analogWrite(ML_PWM, 200); // Ajusta la velocidad de control PWM del motor A a 200
      digitalWrite(MR_Ctrl, LOW); // Pone el pin de control de dirección del motor B a LOW
      analogWrite(MR_PWM, 200); // Ajusta la velocidad de control PWM del motor B a 200

    } 
    
    if (command == 'A') {
      digitalWrite(ML_Ctrl, HIGH); // Pone el pin de control de dirección del motor A a HIGH
      analogWrite(ML_PWM, 200); // Ajusta la velocidad de control PWM del motor A a 200
      digitalWrite(MR_Ctrl, HIGH); // Pone el pin de control de dirección del motor B a HIGH
      analogWrite(MR_PWM, 200); // Ajusta la velocidad de control PWM del motor B a 200

    }

    if (command == 'I') {
      digitalWrite(ML_Ctrl, HIGH); // Pone el pin de control de dirección del motor A a HIGH
      analogWrite(ML_PWM, 50); // Ajusta la velocidad de control PWM del motor A a 200
    }

    if (command == 'D') {
      digitalWrite(MR_Ctrl, HIGH); // Pone el pin de control de dirección del motor B a HIGH
      analogWrite(MR_PWM, 200); // Ajusta la velocidad de control PWM del motor B a 200

    }

    if (command == 'S') {
      analogWrite(ML_PWM, 0); // Ajusta la velocidad de control PWM del motor A a 0
      analogWrite(MR_PWM, 0); // Ajusta la velocidad de control PWM del motor B a 0

    }

  }
  
}

