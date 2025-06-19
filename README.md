#include <iostream>  // Includes input/output stream for using cout and cin
#include <vector>    // Includes vector container from the STL
#include <algorithm> // Includes STL algorithms like swap()

using namespace std; // Allows use of standard namespace without prefixing std::

// Denomination structure
struct Denomination {
    int value;  // Value of the currency note (e.g., 1000, 2000 Rwf)
    int count;  // Number of notes available for this denomination
};

// Base abstract class
class CashDispenser {
protected:
    Denomination* denoms; // Pointer to dynamic array of Denomination
    int size;             // Number of different denominations

public:
    CashDispenser() : denoms(nullptr), size(0) {} // Constructor initializes with no denominations

    virtual ~CashDispenser() { // Destructor to free dynamically allocated memory
        delete[] denoms;
    }

    virtual bool dispense(int amount) = 0; // Pure virtual function for dispensing money

    void addDenomination(int value, int count) { // Adds or updates a denomination
        for (int i = 0; i < size; ++i) {
            if (denoms[i].value == value) {   // If denomination already exists
                denoms[i].count += count;     // Increase its count
                return;
            }
        }

        // Add new denomination if not found
        Denomination* newDenoms = new Denomination[size + 1]; // Create new array with one more slot
        for (int i = 0; i < size; ++i) {
            newDenoms[i] = denoms[i]; // Copy existing denominations
        }
        newDenoms[size].value = value; // Add new denomination value
        newDenoms[size].count = count; // Add new denomination count
        delete[] denoms;               // Free old memory
        denoms =  newDenoms;            // Update pointer to new array
        ++size;                        // Increase size
    }

    void removeDenomination(int value) { // Removes a denomination by value
        int index = -1;
        for (int i = 0; i < size; ++i) {
            if (denoms[i].value == value) { // Find index of the denomination
                index = i;
                break;
            }
        }

        if (index == -1) return; // If not found, do nothing

        Denomination* newDenoms = new Denomination[size - 1]; // Create smaller array
        for (int i = 0, j = 0; i < size; ++i) {
            if (i != index) {
                newDenoms[j++] = denoms[i]; // Copy all except the one to remove
            }
        }
        delete[] denoms; // Free old memory
        denoms = newDenoms; // Update pointer
        --size; // Decrease size
    }

    void showDenoms() { // Print all available denominations and their counts
        for (int i = 0; i < size; ++i) {
            cout << denoms[i].value << " Rwf: " << denoms[i].count << " notes\n";
        }
    }
};

// Greedy Strategy
class GreedyDispenser : public CashDispenser {
public:
    bool dispense(int amount) override { // Override dispense method with greedy approach
        cout << "\n[Greedy] Dispensing " << amount << " Rwf\n";
        for (int i = 0; i < size; ++i) { // Sort denominations in descending order
            for (int j = i + 1; j < size; ++j) {
                if (denoms[j].value > denoms[i].value) {
                    swap(denoms[i], denoms[j]); // Swap if next denomination is larger
                }
            }
        }

        for (int i = 0; i < size; ++i) { // Try to use as many large notes as possible
            int use = min(amount / denoms[i].value, denoms[i].count); // How many notes to use
            if (use > 0) {
                cout << " - " << use << " x " << denoms[i].value << " Rwf\n"; // Print used notes
                denoms[i].count -= use;   // Decrease available notes
                amount -= use * denoms[i].value; // Subtract amount
            }
        }

        if (amount > 0) { // If some amount is left, it could not be dispensed
            cout << "Not enough denominations to dispense remaining: " << amount << " Rwf\n";
            return false;
        }
        return true; // Successfully dispensed
    }
};

// Optimal Strategy (fewest notes)
class OptimalDispenser : public CashDispenser {
public:
    bool dispense(int amount) override { // Override dispense method with optimal strategy
        cout << "\n[Optimal] Dispensing " << amount << " Rwf\n";
        vector<int> dp(amount + 1, 1e9); // Dynamic programming array: minimum notes needed
        vector<int> last(amount + 1, -1); // To remember last note used to reach amount
        dp[0] = 0; // Base case: 0 notes to make 0 Rwf

        for (int i = 0; i < size; ++i) { // For each denomination
            for (int c = 1; c <= denoms[i].count; ++c) { // For each available count of that denomination
                for (int j = amount; j >= denoms[i].value; --j) { // Update DP from back
                    if (dp[j - denoms[i].value] + 1 < dp[j]) { // Check if fewer notes
                        dp[j] = dp[j - denoms[i].value] + 1; // Update with fewer notes
                        last[j] = i; // Save index of denomination used
                    }
                }
            }
        }

        if (dp[amount] == 1e9) { // If not possible to dispense
            cout << "Not possible to dispense optimally.\n";
            return false;
        }

        int a = amount;
        while (a > 0 && last[a] != -1) { // Reconstruct the used denominations
            int idx = last[a];
            cout << " - 1 x " << denoms[idx].value << " Rwf\n"; // Show note used
            denoms[idx].count--; // Decrease note count
            a -= denoms[idx].value; // Decrease remaining amount
        }
         return true;// Successfully dispensed
    }
};

int main() { // Main program starts
    CashDispenser* machines[2]; // Array of two dispenser pointers

    GreedyDispenser* greedy = new GreedyDispenser(); // Create greedy dispenser
    OptimalDispenser* optimal = new OptimalDispenser(); // Create optimal dispenser

    // Add denominations to greedy dispenser
    greedy->addDenomination(5000, 5);
    greedy->addDenomination(2000, 4);
    greedy->addDenomination(1000, 10);

    // Add same denominations to optimal dispenser
    optimal->addDenomination(5000, 5);
    optimal->addDenomination(2000, 4);
    optimal->addDenomination(1000, 10);

    machines[0] = greedy; // Store greedy in array
    machines[1] = optimal; // Store optimal in array

    // Try dispensing 13000 Rwf using both strategies
    machines[0]->dispense(13000); // Greedy
    machines[1]->dispense(13000); // Optimal

    // Show remaining denominations in greedy machine
    cout << "\nRemaining Notes (Greedy):\n";
    greedy->showDenoms();

    // Show remaining denominations in optimal machine
    cout << "\nRemaining Notes (Optimal):\n";
    optimal->showDenoms();

    // Clean up memory
    delete greedy;
    delete optimal;

    return 0; // Program ends
}
