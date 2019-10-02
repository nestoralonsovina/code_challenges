
fn find_missing_letter(chars: &[char]) -> char {
    let n = chars.len();
    let mut res = 0;

    for i in 0..(n - 1) {
        if chars[i] as u8 + 1 != chars[i + 1] as u8 {
            res = (chars[i] as u8) + 1;
        }
    }
    res as char
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_tests() {
        assert_eq!(find_missing_letter(&['a', 'b', 'c', 'd', 'f']), 'e');
        assert_eq!(find_missing_letter(&['O', 'Q', 'R', 'S']), 'P');
    }
}