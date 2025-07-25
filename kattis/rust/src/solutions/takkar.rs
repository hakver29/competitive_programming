
use std::io::{self, BufRead};

/// Compares the size of Trump's and Kim's buttons.
///
/// Returns:
/// - `"MAGA!"` if Trump's button is bigger
/// - `"FAKE NEWS!"` if Kim's button is bigger
/// - `"WORLD WAR 3!"` if they are equal
fn compare_buttons(trump: i32, kim: i32) -> &'static str {
    if trump > kim {
        "MAGA!"
    } else if trump < kim {
        "FAKE NEWS!"
    } else {
        "WORLD WAR 3!"
    }
}

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let trump = lines
        .next()
        .expect("Missing first input line")
        .expect("Error reading input")
        .trim()
        .parse::<i32>()
        .expect("Invalid integer");

    let kim = lines
        .next()
        .expect("Missing second input line")
        .expect("Error reading input")
        .trim()
        .parse::<i32>()
        .expect("Invalid integer");

    println!("{}", compare_buttons(trump, kim));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_trump_bigger() {
        assert_eq!(compare_buttons(420, 42), "MAGA!");
    }

    #[test]
    fn test_kim_bigger() {
        assert_eq!(compare_buttons(7, 13), "FAKE NEWS!");
    }

    #[test]
    fn test_equal_buttons() {
        assert_eq!(compare_buttons(1337, 1337), "WORLD WAR 3!");
    }

    #[test]
    fn test_negative_buttons() {
        assert_eq!(compare_buttons(-1, -5), "MAGA!");
        assert_eq!(compare_buttons(-10, -1), "FAKE NEWS!");
        assert_eq!(compare_buttons(-3, -3), "WORLD WAR 3!");
    }

    #[test]
    fn test_zero_buttons() {
        assert_eq!(compare_buttons(0, 0), "WORLD WAR 3!");
        assert_eq!(compare_buttons(0, 1), "FAKE NEWS!");
        assert_eq!(compare_buttons(1, 0), "MAGA!");
    }
}

