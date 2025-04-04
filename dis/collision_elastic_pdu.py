from enum import Enum

from .siso_ref_010.enums.dis_pdu_type import DisPduType
from .entity_information_interaction_family_pdu import EntityInformationInteractionFamilyPdu
from .vector3float import Vector3Float
from .entity_id import EntityID
from .event_identifier import EventIdentifier

class CollisionElasticPdu( EntityInformationInteractionFamilyPdu ):
    """7.2.4 Information about elastic collisions in a DIS exercise shall be communicated using a Collision-Elastic PDU. See 5.3.4."""

    def __init__(self):
        """ Initializer for CollisionElasticPdu"""
        super().__init__()
        """ This field shall identify the entity that is issuing the PDU and shall be represented by an Entity Identifier record (see 6.2.28)"""
        self.issuingEntityID = EntityID()
        """ This field shall identify the entity that has collided with the issuing entity. This field shall be a valid identifier of an entity or server capable of responding to the receipt of this Collision-Elastic PDU. This field shall be represented by an Entity Identifier record (see 6.2.28)."""
        self.collidingEntityID = EntityID()
        """ This field shall contain an identification generated by the issuing simulation application to associate related collision events. This field shall be represented by an Event Identifier record (see 6.2.34)."""
        self.collisionEventID = EventIdentifier()
        """ some padding"""
        self.pad = 0
        """ This field shall contain the velocity at the time the collision is detected at the point the collision is detected. The velocity shall be represented in world coordinates. This field shall be represented by the Linear Velocity Vector record [see 6.2.95 item c)]"""
        self.contactVelocity = Vector3Float()
        """ This field shall contain the mass of the issuing entity and shall be represented by a 32-bit floating point number representing kilograms"""
        self.mass = 0.0
        """ This field shall specify the location of the collision with respect to the entity with which the issuing entity collided. This field shall be represented by an Entity Coordinate Vector record [see 6.2.95 item a)]."""
        self.locationOfImpact = Vector3Float()
        """ These six records represent the six independent components of a positive semi-definite matrix formed by pre-multiplying and post-multiplying the tensor of inertia, by the anti-symmetric matrix generated by the moment arm, and shall be represented by 32-bit floating point numbers (see 5.3.4.4)"""
        self.collisionIntermediateResultXX = 0.0
        """ tensor values"""
        self.collisionIntermediateResultXY = 0.0
        """ tensor values"""
        self.collisionIntermediateResultXZ = 0.0
        """ tensor values"""
        self.collisionIntermediateResultYY = 0.0
        """ tensor values"""
        self.collisionIntermediateResultYZ = 0.0
        """ tensor values"""
        self.collisionIntermediateResultZZ = 0.0
        """ This record shall represent the normal vector to the surface at the point of collision detection. The surface normal shall be represented in world coordinates. This field shall be represented by an Entity Coordinate Vector record [see 6.2.95 item a)]."""
        self.unitSurfaceNormal = Vector3Float()
        """ This field shall represent the degree to which energy is conserved in a collision and shall be represented by a 32-bit floating point number. In addition, it represents a free parameter by which simulation application developers may "tune" their collision interactions."""
        self.coefficientOfRestitution = 0.0
        self.pduType = DisPduType.collision_elastic

    def to_string(self) ->str:
        outputString = ""
        outputString += super().to_string()
        outputString += "IssuingEntityID :" + "\n" + self.issuingEntityID.to_string() + "\n"
        outputString += "CollidingEntityID :" + "\n" + self.collidingEntityID.to_string() + "\n"
        outputString += "CollisionEventID :" + "\n" + self.collisionEventID.to_string() + "\n"
        outputString += "Pad : " + str(self.pad) + "\n"
        outputString += "ContactVelocity :" + "\n" + self.contactVelocity.to_string() + "\n"
        outputString += "Mass : " + str(self.mass) + "\n"
        outputString += "LocationOfImpact :" + "\n" + self.locationOfImpact.to_string() + "\n"
        outputString += "CollisionIntermediateResultXX : " + str(self.collisionIntermediateResultXX) + "\n"
        outputString += "CollisionIntermediateResultXY : " + str(self.collisionIntermediateResultXY) + "\n"
        outputString += "CollisionIntermediateResultXZ : " + str(self.collisionIntermediateResultXZ) + "\n"
        outputString += "CollisionIntermediateResultYY : " + str(self.collisionIntermediateResultYY) + "\n"
        outputString += "CollisionIntermediateResultYZ : " + str(self.collisionIntermediateResultYZ) + "\n"
        outputString += "CollisionIntermediateResultZZ : " + str(self.collisionIntermediateResultZZ) + "\n"
        outputString += "UnitSurfaceNormal :" + "\n" + self.unitSurfaceNormal.to_string() + "\n"
        outputString += "CoefficientOfRestitution : " + str(self.coefficientOfRestitution) + "\n"
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
        super( CollisionElasticPdu, self ).serialize(outputStream)
        self.issuingEntityID.serialize(outputStream)
        self.collidingEntityID.serialize(outputStream)
        self.collisionEventID.serialize(outputStream)
        outputStream.write_short(int(self.pad))
        self.contactVelocity.serialize(outputStream)
        outputStream.write_float(int(self.mass))
        self.locationOfImpact.serialize(outputStream)
        outputStream.write_float(int(self.collisionIntermediateResultXX))
        outputStream.write_float(int(self.collisionIntermediateResultXY))
        outputStream.write_float(int(self.collisionIntermediateResultXZ))
        outputStream.write_float(int(self.collisionIntermediateResultYY))
        outputStream.write_float(int(self.collisionIntermediateResultYZ))
        outputStream.write_float(int(self.collisionIntermediateResultZZ))
        self.unitSurfaceNormal.serialize(outputStream)
        outputStream.write_float(int(self.coefficientOfRestitution))

    def parse(self, inputStream):
        """"Parse a message. This may recursively call embedded objects."""
        super( CollisionElasticPdu, self).parse(inputStream)
        self.issuingEntityID.parse(inputStream)
        self.collidingEntityID.parse(inputStream)
        self.collisionEventID.parse(inputStream)
        self.pad = inputStream.read_short()
        self.contactVelocity.parse(inputStream)
        self.mass = inputStream.read_float()
        self.locationOfImpact.parse(inputStream)
        self.collisionIntermediateResultXX = inputStream.read_float()
        self.collisionIntermediateResultXY = inputStream.read_float()
        self.collisionIntermediateResultXZ = inputStream.read_float()
        self.collisionIntermediateResultYY = inputStream.read_float()
        self.collisionIntermediateResultYZ = inputStream.read_float()
        self.collisionIntermediateResultZZ = inputStream.read_float()
        self.unitSurfaceNormal.parse(inputStream)
        self.coefficientOfRestitution = inputStream.read_float()

    # Get the number of attributes defined by SISO
    def get_design_attribute_count(self) -> int:
        return 15

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



