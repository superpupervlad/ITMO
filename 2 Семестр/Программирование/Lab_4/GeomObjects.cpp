#include "GeomObjects.h"
#include <math.h>
#include <iostream>

CVector2D::CVector2D (){
    x_ = 0,
    y_ = 0;
}

CVector2D::CVector2D (double x, double y){
    x_ = x;
    y_ = y;
}

void CVector2D::PrintVector (){
    std::cout << "X: " << this->x_ << " Y: " << this->y_ << "\n";
}

CVector2D operator* (const CVector2D& a, double b){
    CVector2D v(a.x_*b, a.y_*b);
    return v;
}

CVector2D operator+ (const CVector2D& a, const CVector2D& b){
    CVector2D v(a.x_ + b.x_, a.y_ + b.y_);
    return v;
}

CVector2D operator/ (const CVector2D& a, double b){
    CVector2D v(a.x_/b, a.y_/b);
    return v;
}

double AllInOne::mass () const{
    return m;
}

bool AllInOne::operator== (const IPhysObject& obj) const{
    return this->mass() == obj.mass();
}

bool AllInOne::operator< (const IPhysObject& obj) const{
    return this->mass() < obj.mass();
}

unsigned AllInOne::size(){
    return sizeof(*this);
}

Circle::Circle (){
    this->initFromDialogue();
}

Circle::~Circle () = default;

double Circle::square (){
    return M_PI * pow(r, 2);
}

double Circle::perimeter (){
    return 2*M_PI*r;
}


CVector2D Circle::position (){
    return center;
}



void Circle::draw (){
    std::cout << "\n";
    std::cout << "\t/‾‾‾‾\\ \n";
    std::cout << "\t|    |\n";
    std::cout << "\t\\____/  ";
    std::cout << "\nFigure:\t" << name;
    std::cout << "\nRadius:\t" << r;
    std::cout << "\nMass:\t" << m;
    std::cout << "\nPosition:";
    center.PrintVector();
    std::cout << "Size:\t" << size() << "\n";
    std::cout << "\n";
}

void Circle::initFromDialogue(){
    double x, y;
    std::cout << "\nEnter center: ";
    std::cin >> center.x_ >> center.y_;
    std::cout << "\nEnter radius: ";
    std::cin >> r;
    std::cout << "\nEnter mass: ";
    std::cin >> m;
    std::cout << "\n";
}

const char* Circle::classname(){
    return name;
}

Rectangle::Rectangle (){
    this->initFromDialogue();
}

Rectangle::~Rectangle () = default;

double Rectangle::square(){
    return a*b;
}

double Rectangle::perimeter(){
    return a*2 + b*2;
}

CVector2D Rectangle::position (){
    return center;
}

void Rectangle::draw (){
    std::cout << "\n";
    std::cout << "\t|‾‾‾‾|\n";
    std::cout << "\t|    |\n";
    std::cout << "\t|    |\n";
    std::cout << "\t|____|\n";
    std::cout << "\nFigure:\t" << name;
    std::cout << "\nFirst side:\t" << a;
    std::cout << "\nSecond side:\t" << b;
    std::cout << "\nMass:\t" << m;
    std::cout << "\nPosition:";
    center.PrintVector();
    std::cout << "Size:\t" << size() << "\n";
}

void Rectangle::initFromDialogue (){
    double x, y;
    std::cout << "\nEnter length of sides: ";
    std::cin >> a >> b;
    std::cout << "\nEnter center: ";
    std::cin >> center.x_ >> center.y_;
    std::cout << "\nEnter alpha degree: ";
    std::cin >> alpha;
    std::cout << "\nEnter mass: ";
    std::cin >> m;
    std::cout << "\n";
}

const char* Rectangle::classname (){
    return name;
}
