stk.v.12.0
WrittenBy    STK_v12.0.1

BEGIN Planet

    Name		 Mars

    BEGIN PathDescription

        CentralBody		 Mars
        UseCbEphemeris		 Yes

        BEGIN EphemerisData

            EphemerisSource		 None

            JplIndex		 3

            JplSpiceId		 499

            ApplyTDTtoTDBCorrectionForDE		 Yes

            OrbitEpoch		  2.4515450000000000e+06
            OrbitCrdSys		 EclipticJ2000ICRF
            OrbitCrdSysEpoch		  2.4515450000000000e+06
            OrbitParentGM		  1.3271244004193939e+20
            OrbitMeanDist		  2.2794382242757306e+11
            OrbitEcc		  9.3394099999999994e-02
            OrbitInc		  1.8496914200000001e+00
            OrbitRAAN		  4.9559538910000001e+01
            OrbitPerLong		 -2.3943629590000000e+01
            OrbitMeanLong		 -4.5534320500000005e+00
            OrbitMeanDistDot		  7.5648806894702261e+01
            OrbitEccDot		  2.1579739904175222e-09
            OrbitIncDot		 -2.2262313483915126e-07
            OrbitRAANDot		 -8.0102239561943890e-06
            OrbitPerLongDot		  1.2167306776180699e-05
            OrbitMeanLongDot		  5.2403292772046550e-01

        END EphemerisData

    END PathDescription

    BEGIN PhysicalData

        GM		  4.2828375641000000e+13
        Radius		  3.3961900000000000e+06
        Magnitude		  0.0000000000000000e+00
        ReferenceDistance		  0.0000000000000000e+00

    END PhysicalData

    BEGIN AutoRename

        AutoRename		 Yes

    END AutoRename

    BEGIN Extensions

        BEGIN ExternData
        END ExternData

        BEGIN ADFFileData
        END ADFFileData

        BEGIN AccessConstraints
            LineOfSight IncludeIntervals

            UsePreferredMaxStep Yes
            PreferredMaxStep 360
        END AccessConstraints

        BEGIN Desc
            BEGIN ShortText

            END ShortText
            BEGIN LongText

            END LongText
        END Desc

        BEGIN Crdn
            BEGIN AXES
                Type		 AXES_GENALIGNED
                Name		 Inertial3
                Description		 <Enter description (up to 300 chars)>
                Alignment		
                 0.0000000000000000e+00
                 0.0000000000000000e+00
                 1.0000000000000000e+00
                AlignmentUiSequence		 123
                AlignmentUiCoordType		 4
                AlignmentReference		
                BEGIN VECTOR
                    Type		 VECTOR_LINKTO
                    Name		 EclipticNormal
                    RelativePath		 Planet/Deimos
                END VECTOR
                AlignmentLimit		  0.0000000000000000e+00
                Constraint		
                 1.0000000000000004e+00
                 0.0000000000000000e+00
                 0.0000000000000000e+00
                ConstraintUiSequence		 123
                ConstraintUiCoordType		 4
                ConstraintReference		
                BEGIN VECTOR
                    Type		 VECTOR_LINKTO
                    Name		 Sun
                END VECTOR
                ConstraintLimit		  0.0000000000000000e+00
                BodySpin		 Yes
                UniDirConstraint		 No
                LabelX		 X
                LabelY		 Y
                LabelZ		 Z
            END AXES
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Inertial
                Description		 <Enter description (up to 300 chars)>
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MeanEclpJ2000
                    RelativePath		 Planet/Phobos
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_SURFACE
                Name		 Inertial2
                Description		 <Enter description (up to 300 chars)>
                CentralBody		 Mars
                UseMSL		 No
                LLA		  0.0000000000000000e+00  0.0000000000000000e+00  0.0000000000000000e+00
                ClockAngle		  0.0000000000000000e+00
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Inertial3
                Description		 <Enter description (up to 300 chars)>
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial3
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Inertial4
                Description		 <Enter description (up to 300 chars)>
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Mars
                END AXES
            END SYSTEM
        END Crdn

        BEGIN Graphics

            BEGIN Attributes

                MarkerColor		 #ff0e0e
                LabelColor		 #ff0e0e
                LineColor		 #ff0e0e
                LineStyle		 0
                LineWidth		 1
                MarkerStyle		 2
                FontStyle		 0

            END Attributes

            BEGIN Graphics

                Show		 On
                Inherit		 Off
                ShowLabel		 On
                ShowPlanetPoint		 On
                ShowSubPlanetPoint		 Off
                ShowSubPlanetLabel		 Off
                ShowOrbit		 On
                NumOrbitPoints		 360
                OrbitTime		  5.9352808371655308e+07
                OrbitDisplay		                OneOrbit		
                TransformTrajectory		 On

            END Graphics
        END Graphics

        BEGIN VO
        END VO

    END Extensions

END Planet

