class LessonParser:
    '''Parses a given file into a list of lessons.
    Parameters
    ----------
    path : string
        Path to the file to be parsed.
    Returns
    -------
    Lesson[]
    '''
    def parse(self, path):
        raise NotImplementedError('parse not implemented!');

    '''Returns supported file extensions.
    Returns
    -------
    string[]
    '''
    def getSupportedExtensions(self):
        raise NotImplementedError('getSupportedExtensions not implemented!');


    '''Returns if it can parse a given file.
    Parameters
    ----------
    path : string
        Path to the file that is to be parsed.
    '''
    def canParse(self, path):
        raise NotImplementedError('canParse not implemented!');

