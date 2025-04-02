from enum import Enum

from .uafundamental_parameter import UAFundamentalParameter

class UABeam( object ):
    """Information for one or more acoustic beams that the system has, including: length of the beam data,  beam identification number for each beam, and fundamental parametric data used to define the entity’s active emissions.  This field defines the active  emission  parameter  index,  beam  scan  pattern,  orientation,  and beamwidth, which can vary dynamically during system operation."""

    def __init__(self):
        """ Initializer for UABeam"""
        self.beamDataLength = 0
        self.beamNumber = 0
        """ zero-filled array of padding bits for byte alignment and consistent sizing of PDU data"""
        self.padding = 0
        # fundamentalParameterData is an undescribed parameter... 
        self.fundamentalParameterData = UAFundamentalParameter()

    def to_string(self) ->str:
        outputString = ""
        outputString += "BeamDataLength : " + str(self.beamDataLength) + "\n"
        outputString += "BeamNumber : " + str(self.beamNumber) + "\n"
        outputString += "Padding : " + str(self.padding) + "\n"
        outputString += "FundamentalParameterData :" + "\n" + self.fundamentalParameterData.to_string() + "\n"
        return outputString

    def __str__(self):
        return self.to_string()

    def serialize_enum(self, enumValue, outputStream):
        enumSize = enumValue.get_marshaled_size()
        marshallers = {8 : 'byte', 16 : 'short', 32 : 'int'}
        marshalFunction = getattr(outputStream, 'write_unsigned_' + marshallers[enumSize])
        result = marshalFunction(int(enumValue))

    def parse_enum(self, enumValue, intputStream) -> int:
        enumSize = enumValue.get_marshaled_size()
        marshallers = {8 : 'byte', 16 : 'short', 32 : 'int'}
        marshalFunction = getattr(intputStream, 'read_unsigned_' + marshallers[enumSize])
        return marshalFunction()

    def serialize(self, outputStream):
        """serialize the class """
        outputStream.write_byte(int(self.beamDataLength))
        outputStream.write_byte(int(self.beamNumber))
        outputStream.write_short(int(self.padding))
        self.fundamentalParameterData.serialize(outputStream)

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        self.beamDataLength = inputStream.read_byte()
        self.beamNumber = inputStream.read_byte()
        self.padding = inputStream.read_short()
        self.fundamentalParameterData.parse(inputStream)

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 4

    def get_attribute_count(self) -> int:
        attrList = list()
        for attr in dir(self):
            if not callable(getattr(self, attr)):
                if not attr.startswith("__"):
                    if not hasattr(self.__class__.__base__(), attr):
                        attrList.append(attr)
        return len(attrList)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def diff(self,other) -> set:
        diffs = set()
        for key, value in self.__dict__.items():
            value2 = other.__dict__[key]
            if (value != value2):
                if type(value) is list:
                    diffs.add((key, str(value)))
                    diffs.add((key, str(value2)))
                elif (type(value).__module__ == "builtins"):
                    diffs.add((key, value))
                    diffs.add((key, value2))
                elif (isinstance(value, Enum)):
                    diffs.add((key, value))
                    diffs.add((key, value2))
                elif (isinstance(value, object)):
                    diffs.update(value.diff(value2))
                else:
                    diffs.add((key, value))
                    diffs.add((key, value2))
        return(diffs)



