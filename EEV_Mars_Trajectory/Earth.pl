stk.v.12.0
WrittenBy    STK_v12.0.1

BEGIN Planet

    Name		 Earth

    BEGIN PathDescription

        CentralBody		 Earth
        UseCbEphemeris		 Yes

        BEGIN EphemerisData

            EphemerisSource		 JplDE

            JplIndex		 2

            JplSpiceId		 399

            ApplyTDTtoTDBCorrectionForDE		 Yes

            OrbitEpoch		  2.4515450000000000e+06
            OrbitCrdSys		 EclipticJ2000ICRF
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
            OrbitIncDot		 -3.5446078028747444e-07
            OrbitRAANDot		  0.0000000000000000e+00
            OrbitPerLongDot		  8.8507498973305977e-06
            OrbitMeanLongDot		  9.8560910197973994e-01

        END EphemerisData

    END PathDescription

    BEGIN PhysicalData

        GM		  3.9860044150000000e+14
        Radius		  6.3781370000000000e+06
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
        END Desc

        BEGIN Crdn
        END Crdn

        BEGIN Graphics

            BEGIN Attributes

                MarkerColor		 #0e42ff
                LabelColor		 #0e42ff
                LineColor		 #0e42ff
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
                OrbitTime		  3.1568884236888289e+07
                OrbitDisplay		                OneOrbit		
                TransformTrajectory		 On

            END Graphics
        END Graphics

        BEGIN VO
        END VO

    END Extensions

END Planet

