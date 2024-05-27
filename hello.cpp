class Calculator {
public:
    int add(int a, int b) {
        return a + b;
    }
};

extern "C" {
    Calculator* Calculator_new() { return new Calculator(); }
    int Calculator_add(Calculator* calc, int a, int b) { return calc->add(a, b); }
}
