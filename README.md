```ascii
                           **                 
                          /**                 
  *****   ******   ****** /**  ******   ******
 **///** //////** //**//* /** **////** **//// 
/**  //   *******  /** /  /**/**   /**//***** 
/**   ** **////**  /**    /**/**   /** /////**
//***** //********/***    ***//******  ****** 
 /////   //////// ///    ///  //////  //////  
```

# Carlos Organizator 📁✨

A Python program that automates file organization in directories by categorizing files into folders based on their extensions.

---
##⚠️ Important Security Notes

#Windows

The executable was created using PyInstaller. Due to the way PyInstaller packages Python applications, Windows Defender might flag it as potentially unsafe. This is a false positive. To run the program:

- Right-click the executable and select "Properties"
- Check the "Unblock" box next to "This file came from another computer"
- Click "Apply" and "OK"

Alternatively, to add an exception in Windows Defender:

- Open Windows Security
- Go to "Virus & threat protection"
- Click "Manage settings" under "Virus & threat protection settings"
- Scroll down to "Exclusions" and click "Add or remove exclusions"
- Click "Add an exclusion" and select "File"
- Browse to the Carlos Organizator executable
- Click "Select" to add the exclusion

#macOS
When trying to run the program on macOS, you might see a message saying "cannot be opened because it is from an unidentified developer". To run the program:

- Control-click (or right-click) the app
- Select "Open" from the shortcut menu
- Click "Open" in the dialog box
- The app will be saved as an exception to your security settings

----

## 🌟 Features

- Automatic file organization based on predefined categories
- User-friendly interface
- Real-time progress bar
- Duplicate file handling
- Support for over 100 file extensions
- Automatic folder creation as needed

## 📂 Organization Categories

The program organizes files into the following categories:

- Audio
- Spreadsheets
- Videos
- Documents
- Images
- Compressed Files
- Code
- Fonts
- Backup
- Books
- Scripts
- Web
- Data
- Presentations
- System Files
- Design
- Professional Audio Files
- Professional Video Files
- Professional Image Files
- CAD Files
- 3D Animation and Modeling Files
- Game Files
- Architecture Files
- Others (for unrecognized extensions)

## 🚀 How to Use

1. Run the program
2. Choose an option:
   - `1` - Organize current folder
   - `2` - Organize another folder (specify path)
   - `3` - Exit program
3. Wait for the organization process to complete
4. Check the organization summary

## ⚙️ System Requirements

- Python 3.x
- Operating System: Windows, Linux, or macOS
- Read and write permissions in the target directory

## 🔒 Security Features

The program:
- Doesn't move hidden files
- Doesn't move its own executable
- Verifies write permissions before starting
- Handles duplicate files safely

## 🛠️ Technical Features

- Automatic home path expansion (~)
- Conversion to absolute paths
- Directory validation
- Comprehensive error handling
- Countdown system for program termination
- Custom progress bar

## 📝 Usage Notes

- Files with the same name at destination will receive a numeric suffix
- The program ignores hidden files (starting with dot)
- An "Others" folder is automatically created for unrecognized extensions
- A detailed summary is displayed after organization completes

## 👨‍💻 Author

Carlos Schettni

## 📌 Version

1.1 - December 2024

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Add support for more extensions
- Improve documentation

## ⚠️ Disclaimer

This program is not responsible for any data loss. It's recommended to backup your files before use.
