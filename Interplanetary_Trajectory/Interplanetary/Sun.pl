stk.v.12.0
WrittenBy    STK_v12.0.1

BEGIN Planet

    Name		 Sun

    BEGIN PathDescription

        CentralBody		 Sun
        UseCbEphemeris		 Yes

        BEGIN EphemerisData

            EphemerisSource		 None

            JplIndex		 10

            JplSpiceId		 10

            ApplyTDTtoTDBCorrectionForDE		 Yes

            OrbitEpoch		  2.4515450000000000e+06
            OrbitCrdSysEpoch		  2.4515450000000000e+06
            OrbitParentGM		  1.3271244004193939e+20
            OrbitMeanDist		  1.4959826115044250e+11
            OrbitEcc		  1.6711230000000001e-02
            OrbitInc		 -1.5310000000000001e-05
            OrbitRAAN		  0.0000000000000000e+00
            OrbitPerLong		  1.0293768193000000e+02
            OrbitMeanLong		  1.0046457166000002e+02
            OrbitMeanDistDot		  2.3018207620369612e+01
            OrbitEccDot		 -1.2024640657084188e-09
            OrbitIncDot		 -3.5446078028747439e-07
            OrbitRAANDot		  0.0000000000000000e+00
            OrbitPerLongDot		  8.8507498973305960e-06
            OrbitMeanLongDot		  9.8560910197973994e-01

        END EphemerisData

    END PathDescription

    BEGIN PhysicalData

        GM		  1.3271244004193939e+20
        Radius		  6.9570000000000000e+08
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

                MarkerColor		 #fffc57
                LabelColor		 #fffc57
                LineColor		 #fffc57
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
                ShowSubPlanetLabel		 On
                ShowOrbit		 On
                NumOrbitPoints		 360
                OrbitTime		  0.0000000000000000e+00
                OrbitDisplay		                OneOrbit		
                TransformTrajectory		 On

            END Graphics
        END Graphics

        BEGIN VO
        END VO

    END Extensions

END Planet

