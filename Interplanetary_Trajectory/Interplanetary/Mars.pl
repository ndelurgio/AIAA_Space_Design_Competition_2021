stk.v.12.0
WrittenBy    STK_v12.0.1

BEGIN Planet

    Name		 Mars

    BEGIN PathDescription

        CentralBody		 Mars
        UseCbEphemeris		 Yes

        BEGIN EphemerisData

            EphemerisSource		 JplDE

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

            UsePreferredMaxStep No
            PreferredMaxStep 360
        END AccessConstraints

        BEGIN Desc
        END Desc

        BEGIN Crdn
        END Crdn

        BEGIN Graphics

            BEGIN Attributes

                MarkerColor		 #ff820e
                LabelColor		 #ff820e
                LineColor		 #ff820e
                LineStyle		 0
                LineWidth		 1
                MarkerStyle		 2
                FontStyle		 0

            END Attributes

            BEGIN Graphics

                Show		 On
                Inherit		 On
                ShowLabel		 On
                ShowPlanetPoint		 On
                ShowSubPlanetPoint		 On
                ShowSubPlanetLabel		 On
                ShowOrbit		 Off
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

