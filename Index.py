def process_file():
    """Main function to handle file processing with error handling"""
    print("=== File Processing Program ===")
    
    # Get filename from user with error handling
    while True:
        filename = input("Enter the name of the file to process: ")
        try:
            # Read the file
            with open(filename, 'r') as file:
                content = file.read()
            break
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied when accessing '{filename}'. Please try another file.")
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory, not a file. Please enter a valid filename.")
        except UnicodeDecodeError:
            print(f"Error: Could not decode '{filename}'. Please provide a text file.")
        except Exception as e:
            print(f"Unexpected error: {str(e)}. Please try again.")

    # Process the content
    word_count = len(content.split())
    modified_content = content.upper()
    
    # Generate output filename
    output_filename = f"processed_{filename}"
    
    # Write to new file with error handling
    try:
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            output_file.write(f"\n\n=== STATISTICS ===\n")
            output_file.write(f"Word count: {word_count}\n")
            output_file.write(f"Character count: {len(content)}\n")
            output_file.write(f"Line count: {len(content.splitlines())}\n")
        
        print(f"\nSuccess! Processed file saved as '{output_filename}'")
        print(f"Statistics: {word_count} words, {len(content)} characters, {len(content.splitlines())} lines")
    except Exception as e:
        print(f"Error writing to file: {str(e)}")

if __name__ == "__main__":
    process_file()