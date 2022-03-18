stk.v.12.0
WrittenBy    STK_v12.0.1

BEGIN Planet

    Name		 Phobos

    BEGIN PathDescription

        CentralBody		 Phobos
        UseCbEphemeris		 Yes

        BEGIN EphemerisData

            EphemerisSource		 None

            JplIndex		 -1

            JplSpiceId		 401

            ApplyTDTtoTDBCorrectionForDE		 Yes

            OrbitEpoch		  2.4478925006618500e+06
            OrbitCrdSys		 Inertial
            OrbitCrdSysEpoch		  2.4515450000000000e+06
            OrbitMeanDist		  9.3898210362732708e+06
            OrbitEcc		  1.6425539999999999e-02
            OrbitInc		  1.0872065600000000e+00
            OrbitRAAN		  3.1992159021999998e+02
            OrbitPerLong		  2.7067578820000000e+02
            OrbitMeanLong		  5.5057509207359999e+02
            OrbitMeanDistDot		  0.0000000000000000e+00
            OrbitEccDot		  0.0000000000000000e+00
            OrbitIncDot		  0.0000000000000000e+00
            OrbitRAANDot		  0.0000000000000000e+00
            OrbitPerLongDot		  0.0000000000000000e+00
            OrbitMeanLongDot		  1.1259413111230001e+03

        END EphemerisData

    END PathDescription

    BEGIN PhysicalData

        GM		  7.0933990000000002e+05
        Radius		  1.3000000000000000e+04
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

            UsePreferredMaxStep No
            PreferredMaxStep 360
        END AccessConstraints

        BEGIN Desc
            BEGIN ShortText

            END ShortText
            BEGIN LongText

            END LongText
        END Desc

        BEGIN Crdn
        END Crdn

        BEGIN Graphics

            BEGIN Attributes

                MarkerColor		 #c42000
                LabelColor		 #c42000
                LineColor		 #00ffff
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
                OrbitTime		  2.7576774730319714e+04
                OrbitDisplay		                OneOrbit		
                TransformTrajectory		 On

            END Graphics
        END Graphics

        BEGIN VO
        END VO

    END Extensions

END Planet

