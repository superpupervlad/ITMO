#pragma once
//#include <fstream>

class IGeoFig {
public:
    virtual double square() = 0;
    virtual double perimeter() = 0;
};
// Вектор
class CVector2D {
public:
    double x_ = 0;
    double y_ = 0;
    CVector2D ();
    CVector2D (double, double);
    void PrintVector ();
};

CVector2D operator* (const CVector2D&, double);
CVector2D operator+ (const CVector2D&, const CVector2D&);
CVector2D operator/ (const CVector2D&, double);

// Интерфейс "Физический объект".
class IPhysObject {
public:
    virtual double mass() const = 0;
    // Координаты центра масс, м.
    virtual CVector2D position() = 0;
    // Сравнение по массе.
    virtual bool operator== (const IPhysObject&) const = 0;
    virtual bool operator< (const IPhysObject&) const = 0;
};
// Интерфейс "Отображаемый"
class IPrintable {
public:
    virtual void draw() = 0;
};
// Интерфейс для классов, которые можно задать через диалог с пользователем.
class IDialogueInitiable {
    // Задать параметры объекта с помощью диалога с пользователем.
    virtual void initFromDialogue() = 0;
};
// Интерфейс "Класс"
class BaseCObject {
public:
    // Имя класса (типа данных).
    virtual const char * classname() = 0;
    // Размер занимаемой памяти.
    virtual unsigned int size() = 0;
};

class AllInOne : public IGeoFig, public CVector2D, public IPhysObject, public IPrintable, public IDialogueInitiable, public BaseCObject{
public:
    bool operator== (const IPhysObject& obj) const override;
    bool operator< (const IPhysObject& obj) const override;
    double mass() const override;
    unsigned int size() override;
protected:
    double m = 0;
};

class Circle : public AllInOne{
public:
    Circle();
    ~Circle();
    double square() override;
    double perimeter() override;
    CVector2D position() override;
    void draw() override;
    void initFromDialogue() override;
    const char* classname() override;
private:
    CVector2D center;
    double r = 0;
    const char* name = "Circle";
};

class Rectangle : public AllInOne{
public:
    Rectangle();
    ~Rectangle();
    double square() override;
    double perimeter() override;
    CVector2D position() override;
    void draw() override;
    void initFromDialogue() override;
    const char* classname() override;
private:
    CVector2D center;
    double a = 0;
    double b = 0;
    double alpha = 0;
    const char* name = "Rectangle";
};
