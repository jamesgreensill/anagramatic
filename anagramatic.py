import os

if __name__ == "__main__":
    with open("data\\words.txt", "r") as file:
        lines = file.readlines()
        anagrams = {}
        all_anagram_words = set()  # To store all words that are part of anagrams

        if not os.path.exists("output"):
            os.mkdir("output")

        # Process each line to sort alphabetically and group anagrams
        for line in lines:
            # Remove new lines and spaces
            clean_line = line.strip()
            # Sort the line alphabetically
            sorted_line = "".join(sorted(clean_line, key=str.lower))
            # Initialise empty list if the key does not exist, and append the word.
            anagrams.setdefault(sorted_line, []).append(clean_line)

        # Filter all anagrams that do not have more than 1 entry
        filtered_anagrams = {key: value for key,
                             value in anagrams.items() if len(value) > 1}

        # Collect all words that are part of anagrams
        for words in filtered_anagrams.values():
            all_anagram_words.update(words)

        # Get the length of unique anagrams
        unique_anagrams = len(filtered_anagrams)

        # Get the length of all anagrams
        total_words_in_groups = sum(len(words)
                                    for words in filtered_anagrams.values())

        # Get the length of the initial data-set
        total_words_in_file = len(lines)

        # Calculate the percentage of anagrams vs. data-set
        percentage_in_anagrams = (
            total_words_in_groups / total_words_in_file) * 100

        # Calculate the percentage of unique anagrams vs. data-set
        percentage_in_unique_anagrams = (
            unique_anagrams / total_words_in_file) * 100

        # Sort the anagrams by frequency
        sorted_anagrams = sorted(filtered_anagrams.items(
        ), key=lambda item: len(item[1]), reverse=True)

        # Write the anagrams information to file
        with open("output\\anagrams.txt", "w") as output_file:
            output_file.write(f"Total Anagram Groups: {unique_anagrams}\n")
            output_file.write(f"Total Unique Anagrams: {
                              total_words_in_groups}\n")
            output_file.write(
                f"Total Words in Original Data-set: {total_words_in_file}\n")
            output_file.write(
                f"Percentage of Anagrams vs. Data-set: {percentage_in_anagrams:.2f}%\n")
            output_file.write(
                f"Percentage of Unique Anagrams vs. Data-set: {percentage_in_unique_anagrams:.2f}%\n\n")
            for key, value in sorted_anagrams:
                count = len(value)
                output_file.write(f"{count}: {', '.join(value)}\n")

        # Filter out anagram words from the original list
        non_anagram_words = [
            line.strip() for line in lines if line.strip() not in all_anagram_words]

        # Write non-anagram words to a new file
        with open("output\\non_anagrams.txt", "w") as non_anagrams_file:
            non_anagrams_file.write("All words that are not anagrams.\n\n")
            non_anagrams_file.write("\n".join(non_anagram_words))
