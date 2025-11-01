#define ROSSERIAL_ARDUINO_TCP
#define LED_PIN 10

#include "WiFi.h"
#include <ros.h>
#include <std_msgs/Int16.h>
#include <std_msgs/String.h>

const char *ssid = "";
const char *password = "";

// ip of your ROS machine (for Windows, if you use port
// forwarding, it is the IP of Windows and you need to have port forwarding to redirect
// packets to your WSL linux)
IPAddress server(192, 168, 1, 138); 

ros::NodeHandle nh; // the node
std_msgs::String str_msg;  // the type of message that will be sent
std_msgs::Int16 int_msg; // the type of message that will be received
ros::Publisher pub("chatter", &str_msg);  // topic to publish on

void message_callback( const std_msgs::Int16& light_intensity){
  Serial.println("Received message");
  analogWrite(LED_PIN, light_intensity.data);
}
ros::Subscriber<std_msgs::Int16> sub("light_intensity", &message_callback ); // topic to listen on

void setup()
{
  Serial.begin(115200);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) // -> wifi delay -> a must -> other wise it will restart continuously↪
  { 
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected - IP address: ");
  Serial.println(WiFi.localIP());

  pinMode(LED_PIN, OUTPUT);

  // Setup connection to ROS machine (server)
  nh.getHardware()->setConnection(server, 11511);
  nh.initNode();
  // nh.advertise(pub); // the topic must be advertised to the master
  nh.subscribe(sub);
}

void loop()
{
  //Send a HelloWorld message every second
  // std_msgs::String str;
  // str.data = "hello world";
  // Serial.println("Sending message");
  // pub.publish( &str );

  nh.spinOnce(); // Required, otherwise topic not detected by ROS !
  delay(1000);
}
